# import logging
# import azure.functions as func
# import requests
# import smtplib
# from email.mime.text import MIMEText
# from firebase_admin import credentials, firestore, initialize_app

# cred = credentials.Certificate("serviceAccountKey.json")  # Upload your serviceAccountKey to your Azure Function
# initialize_app(cred)
# db = firestore.client()

# def get_rating(handle):
#     url = f"https://codeforces.com/api/user.info?handles={handle}"
#     try:
#         response = requests.get(url).json()
#         if response["status"] == "OK":
#             return response["result"][0].get("rating", 0)
#     except:
#         return None
#     return None

# def send_email(to_email, handle, new_rating):
#     sender_email = "your_email@gmail.com"
#     password = "your_app_password"  # Use App Password if Gmail

#     msg = MIMEText(f"Hi {handle}, your Codeforces rating changed to {new_rating}!")
#     msg["Subject"] = "🎉 Codeforces Rating Update!"
#     msg["From"] = sender_email
#     msg["To"] = to_email

#     try:
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(sender_email, password)
#             server.send_message(msg)
#         logging.info(f"✅ Email sent to {to_email}")
#     except Exception as e:
#         logging.error(f"❌ Failed to send email: {e}")

# app = func.FunctionApp()

# @app.function_name(name="checkCodeforcesRatings")
# @app.schedule(schedule="0 */15 * * * *", arg_name="mytimer", run_on_startup=False, use_monitor=True)
# def check_ratings(mytimer: func.TimerRequest):
#     logging.info("🔁 Running Codeforces rating checker")

#     users = db.collection("users").stream()
#     for user in users:
#         data = user.to_dict()
#         handle = data["handle"]
#         email = data["email"]
#         last_rating = data.get("last_rating", 0)

#         current_rating = get_rating(handle)
#         if current_rating and current_rating != last_rating:
#             send_email(email, handle, current_rating)
#             db.collection("users").document(user.id).update({
#                 "last_rating": current_rating
#             })

import logging
import azure.functions as func
import requests
import smtplib
from email.mime.text import MIMEText
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred)
db = firestore.client()

def get_rating(handle):
    try:
        res = requests.get(f"https://codeforces.com/api/user.info?handles={handle}").json()
        return res["result"][0].get("rating", 0) if res["status"] == "OK" else None
    except:
        return None

def send_email(to_email, handle, new_rating):
    sender = "your_email@gmail.com"
    password = "your_app_password"  # App password, not your login

    msg = MIMEText(f"Hi {handle}, your Codeforces rating is now {new_rating}!")
    msg["Subject"] = "🎉 Codeforces Rating Updated"
    msg["From"] = sender
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        logging.info(f"✅ Email sent to {to_email}")
    except Exception as e:
        logging.error(f"❌ Email failed: {e}")

app = func.FunctionApp()

@app.function_name(name="checkCodeforcesRatings")
@app.schedule(schedule="0 */15 * * * *", arg_name="mytimer", run_on_startup=False, use_monitor=True)
def check_ratings(mytimer: func.TimerRequest):
    logging.info("⏱️ Checking ratings")
    users = db.collection("users").stream()

    for user in users:
        data = user.to_dict()
        handle = data["handle"]
        email = data["email"]
        last_rating = data.get("last_rating", 0)

        current_rating = get_rating(handle)
        if current_rating and current_rating != last_rating:
            send_email(email, handle, current_rating)
            db.collection("users").document(user.id).update({ "last_rating": current_rating })


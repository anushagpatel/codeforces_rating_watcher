import requests
import smtplib
from email.mime.text import MIMEText
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_rating(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url).json()
    if response["status"] == "OK":
        return response["result"][0].get("rating", 0)
    return None

def send_email(to_email, handle, rating):
    msg = MIMEText(f"Hello, your Codeforces rating is now: {rating}")
    msg["Subject"] = "Codeforces Rating Updated"
    msg["From"] = "your-email@gmail.com"
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your-email@gmail.com")
        server.send_message(msg)

def check_and_notify():
    users = db.collection("users").stream()
    for user in users:
        data = user.to_dict()
        handle = data["handle"]
        email = data["email"]
        last_rating = data.get("last_rating", 0)

        current_rating = get_rating(handle)
        if current_rating and current_rating != last_rating:
            send_email(email, handle, current_rating)
            db.collection("users").document(user.id).update({
                "last_rating": current_rating
            })

if __name__ == "__main__":
    check_and_notify()

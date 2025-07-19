import os
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    return func.HttpResponse(html, mimetype="text/html")

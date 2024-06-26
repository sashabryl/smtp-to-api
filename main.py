import os

from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

RESEND_API_URL = "https://api.resend.com/emails"
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
SENDER = os.getenv("SENDER")


@app.post("/forward-email")
async def forward_email(request: Request):
    email_data = await request.json()
    email_data["from"] = SENDER
    authentication_header = request.headers.get("Authorization")
    if authentication_header.split()[1] != SECRET_KEY:
        return {"status": 401, "message": "Unauthorized"}
  
    response = requests.post(
      RESEND_API_URL,
      json=email_data,
      headers={
          "Authorization": f"Bearer {RESEND_API_KEY}",
          "Content-Type": "application/json"
          }
    )
    
    return {"status": response.status_code, "response": response.json()}

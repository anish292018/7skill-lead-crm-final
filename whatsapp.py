import os
import requests

def send_whatsapp(name, phone):
    print("🔥 WhatsApp function CALLED")

    access_token = os.getenv("WHATSAPP_TOKEN")
    phone_id = os.getenv("WHATSAPP_PHONE_ID")
    to_number = os.getenv("TO_WHATSAPP_NUMBER")

    print("Token exists:", bool(access_token))
    print("Phone ID:", phone_id)
    print("To Number:", to_number)

    if not access_token or not phone_id or not to_number:
        print("❌ Missing WhatsApp ENV variables")
        return

    url = f"https://graph.facebook.com/v19.0/{phone_id}/messages"

    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print("WhatsApp HTTP Status:", response.status_code)
    print("WhatsApp API Response:", response.text)

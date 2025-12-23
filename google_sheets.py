import gspread
from google.oauth2.service_account import Credentials

def save_to_google_sheet(name, phone):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(
        "credentials.json", scopes=scopes
    )

    client = gspread.authorize(creds)
    sheet = client.open_by_key("YOUR_SHEET_ID").sheet1

    sheet.append_row([name, phone])

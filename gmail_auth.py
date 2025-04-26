from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def login_to_gmail():
    # DO NOT set redirect_uri manually!
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json',
        SCOPES
    )
    creds = flow.run_local_server(port=8080)  # ← force port 8080
    service = build('gmail', 'v1', credentials=creds)
    return service

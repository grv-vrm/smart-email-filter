from googleapiclient.discovery import build
import base64
import email

def get_recent_emails(service, max_results=10):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    email_list = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        
        payload = msg_data.get('payload', {})
        headers = payload.get('headers', [])

        # Initialize fields
        subject = sender = snippet = ""

        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
            if header['name'] == 'From':
                sender = header['value']

        snippet = msg_data.get('snippet', '')

        email_entry = {
            'sender': sender,
            'subject': subject,
            'snippet': snippet
        }

        email_list.append(email_entry)

    return email_list

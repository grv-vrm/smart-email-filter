import streamlit as st
from gmail_auth import login_to_gmail
from gmail_fetcher import get_recent_emails
from priority_classifier import classify_email_priority

st.title("📧 Smart Email Priority Filter")

if "service" not in st.session_state:
    st.session_state.service = None

if st.button("Login to Gmail"):
    service = login_to_gmail()
    st.session_state.service = service
    st.success("Login successful!")

if st.session_state.service:
    st.header("Your Recent Emails:")
    emails = get_recent_emails(st.session_state.service, max_results=10)

    for email in emails:
        priority = classify_email_priority(email)

        st.subheader(f"[{priority}] {email['subject']}")
        st.write(f"**From:** {email['sender']}")
        st.write(email['snippet'])
        st.write("---")

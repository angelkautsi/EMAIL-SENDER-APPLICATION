import imaplib
import email
from email.header import decode_header
from credentials import email_address, email_password

def get_recent_emails(limit=5):
    try:
        #connecting to the GMAIL'S IMAP server
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(email_address, email_password)
        imap.select("inbox")
import imaplib
import email
from email.header import decode_header
from shlex import split

from credentials import email_address, email_password

def get_recent_emails(limit=5):
    try:
        #connecting to the GMAIL'S IMAP server
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(email_address, email_password)
        imap.select("inbox")

        #searching for all emails in the inbox
        status, messages =  imap.search(None, "All")
        email_ids = messages[0].split()
        recent_ids = email_ids[-limit: ] #getting the most recent emails 'limit'

        emails = []
        for eid in reversed(recent_ids):
            status, msg_data = imap.fetch(eid, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # Safe subject parsing
                    raw_subject = msg["Subject"]
                    if raw_subject is None:
                        subject = "(No Subject)"
                    else:
                        try:
                            subject, encoding = decode_header(raw_subject)[0]
                            if isinstance(subject, bytes):
                                subject = subject.decode(encoding or "utf-8")
                        except:
                            subject = str(raw_subject)

                    # Safe sender
                    from_ = msg.get("From") or "(Unknown sender)"

                    # Safe body
                    body = ""
                    try:
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    payload = part.get_payload(decode=True)
                                    if payload:
                                        body = payload.decode(errors="ignore")
                                    break
                        else:
                            payload = msg.get_payload(decode=True)
                            if payload:
                                body = payload.decode(errors="ignore")
                    except:
                        body = "(Unable to decode message content.)"

                emails.append({
                    "from": from_,
                    "subject": subject,
                    "body": body
                })
        imap.logout()
        print("Emails retrieved:", len(emails))  # Shows how many emails were fetched
        return emails

    except Exception as e:
        print("IMAP ERROR:", e)  # Add this


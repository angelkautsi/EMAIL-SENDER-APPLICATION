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

                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")

                    from_ = msg.get("From")

                    #getting email body
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if content_type == "text/plain":
                                try:
                                    body = part.get_payload(decode=True).decode()
                                    break
                                except:
                                    body = "(Cannot decode body)"
                            else:
                                    body = part.get_payload(decode=True).decode(errors="ignore")

                            emails.append({
                                "from": from_,
                                "subject": subject,
                                "body": body
                            })
            imap.logout()
            return emails

    except Exception as e:
        return[{"subject": "Error", "from": "", "body": str(e)}]

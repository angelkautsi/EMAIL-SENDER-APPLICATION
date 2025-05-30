import smtplib
from email.message import EmailMessage

def send_email(sender, password, recipient, subject, body):
    try:
        #creating the email
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        msg.set_content(body)

        #connecting to SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()

        return True, "Email sent successfully."
    except smtplib.SMTPAuthenticationError:
        return False, "Failed authentication. Check your email or password."
    except smtplib.SMTPRecipientsRefused:
        return  False, "Recipient email incorrect or refused."
    except Exception as e:
        return False, f"An error occurred: {str(e)}"
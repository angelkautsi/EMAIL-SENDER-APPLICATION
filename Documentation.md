## **Project Documentation: Email Sender Application**

---

### 1. **Project Title**

**Email Sender Application**

A Python GUI-based application for sending emails securely using Gmail's SMTP service.

---

### 2. **Objective**

The main objective of this project is to build a **user-friendly email client application** using **Python** and **Kivy GUI** that allows users to:

* Input email details (recipient, subject, message)
* Send emails using Gmail SMTP
* Receive real-time feedback (success or failure)
* Be able to view recent emails from application

This project demonstrates **network programming concepts** and **graphical user interface development**, integrating them into a complete, functional tool.

---

### 3. **Tools & Technologies Used**

| Tool / Library   | Purpose |
|------------------|  |
| **Python 3.13**  | Core programming language |
| **Kivy**         | Cross-platform GUI development |
| **smtplib**      | Python library to interact with SMTP servers |
| **imaplib**      | Gmail mapping library to show recent emails |
| **Git & GitHub** | Version control and source code hosting |

---

### 4. **Why Kivy Was Used**

* **Modern UI**: Kivy provides a modern, mobile-friendly interface compared to older tools like Tkinter.
* **Cross-Platform Support**: Works on Windows, Linux, macOS, and even Android/iOS.
* **Customization**: Kivy’s flexible layout system allowed us to easily design our form-based application.
* **Learning Value**: This project encouraged the exploration of more modern GUI tools beyond basic frameworks.

---

### 5. **Networking Concepts Explained**

This project is based on **Client-Server communication over the SMTP (Simple Mail Transfer Protocol)**:

#### SMTP Process in the App

1. **Connection**: The app connects to Gmail’s SMTP server at `smtp.gmail.com` on port `587`.
2. **TLS Security**: The connection is encrypted using `starttls()` for secure email transfer.
3. **Authentication**: The user logs in using an **App Password** (provided by Gmail with 2FA).
4. **Transmission**: The composed email is sent from the client (our app) to the server (Gmail).
5. **Response Handling**: The app checks if the email was successfully sent or if errors occurred.

### IMAP Connectivity in the App

This application uses **IMAP (Internet Message Access Protocol)** to securely connect to Gmail and retrieve incoming emails.

IMAP allows the app to access messages directly from the Gmail server without downloading them permanently. Using Python’s `imaplib` and `email` libraries, the application:

- Connects to the Gmail IMAP server at `imap.gmail.com` using SSL
- Authenticates using the **App Password**
- Selects the inbox and fetches the latest emails
- Parses each email to extract:
  - **Sender**
  - **Subject**
  - **Body**
- Converts HTML-formatted messages into clean, readable plain text using a custom HTML-stripper function

This functionality powers the **Inbox Viewer** feature inside the app, allowing users to read replies or incoming messages **without leaving the application**.

----

### Key Networking Features Implemented

My application integrates several core networking functionalities using internet protocols and secure communication libraries:

- **SMTP (Simple Mail Transfer Protocol)**  
  Used for sending emails securely through Gmail’s SMTP server (`smtp.gmail.com`) via port 587 with TLS encryption. Handled using Python’s built-in `smtplib`.

- **IMAP (Internet Message Access Protocol)**  
  Enables secure access to Gmail's inbox server (`imap.gmail.com`) using `imaplib`. Messages are retrieved in real-time from the server rather than being stored locally.

- **App Password Authentication**  
  Uses Gmail’s App Password feature (via OAuth-2FA setup) instead of storing raw passwords. This enhances security and supports Gmail’s modern authentication policies.

- **Secure SSL/TLS Connections**  
  All server communications (SMTP and IMAP) are encrypted using SSL or TLS, preventing unauthorized interception of credentials and email content.

- **Real-time Inbox Fetching**  
  The app connects to the Gmail server to fetch and display the latest emails directly inside the application interface without relying on third-party platforms.

- **HTML Message Parsing and Cleanup**  
  Incoming emails that arrive in HTML format are stripped and parsed into readable plain text using custom logic, allowing safe rendering within the app.

---

### 6. **Application Features**

* Easy-to-use interface with labeled input fields
* Input validation (prevents sending with missing info)
* Secure login via Gmail App Passwords
* Success and error feedback shown in real-time
* Modular design with `Email_sender.py` handling all email logic

---

### 7. **Screenshots**

Include the following in the documentation:

* App on startup (GUI window)
* Form filled in
* Success message after sending
* Input validation error
* Email received in Gmail (message received)
* Inbox preview

 All screenshots are saved under:

```
/screenshots/
```

---

### 8. **Project Structure**

```
EMAIL-SENDER-APPLICATION/
├── main_kivy.py           # Main GUI script
├── Email_sender.py        # SMTP email sending logic
├── Email_reader.py        # IMAP inbox viewing logic
├── credentials.py         # Email & app password (excluded via .gitignore)
├── .gitignore             # Prevents sensitive files from being tracked
├── README.md              # Project summary and setup guide
├── screenshots/           # Screenshots for README and presentation
├── requirements.txt       # Python dependencies
```

---

### 9. **Project Outcome**

* Successfully built a cross-platform GUI email sender using Python and Kivy
* Demonstrated secure client-server communication using SMTP
* Learned to work with the Gmail IMAP library to be able to connect my inbox to the application
* Gained experience with GUI layout, error handling, and modular programming
* Maintained proper GitHub version control and documentation

---

### 10. **Submission & Deliverables**

* **GitHub Repository**: https://github.com/angelkautsi/EMAIL-SENDER-APPLICATION.git
* **README.md** with Setup Instructions
* **Screenshots Folder**
* **10-slide PowerPoint** (in `/presentation/`)
* **Working Demonstration App**

---

## End of Documentation

---

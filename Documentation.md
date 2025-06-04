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

This project demonstrates **network programming concepts** and **graphical user interface development**, integrating them into a complete, functional tool.

---

### 3. **Tools & Technologies Used**

| Tool / Library    | Purpose                                        |
|-------------------| ---------------------------------------------- |
| **Python 3.13**   | Core programming language                      |
| **Kivy**          | Cross-platform GUI development                 |
| **smtplib**       | Python library to interact with SMTP servers   |
| **email.message** | To format and structure email content properly |
| **Git & GitHub**  | Version control and source code hosting        |

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

#### Key Networking Features:

* **Client-Server Model**: The app is the client, Gmail SMTP is the server.
* **Port 587**: Standard port for sending email securely using TLS.
* **App Password**: Enhances security by avoiding actual password use in scripts.
* **Error Handling**: Exceptions for login failure, invalid recipients, etc., are managed cleanly.

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

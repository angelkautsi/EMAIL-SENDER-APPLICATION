from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Email_sender import send_email
from credentials import email_address, email_password
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

class EmailForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=12, **kwargs)   #constructor

        self.add_widget(Label(text='Recipient Email')) #recipient button
        self.recipient_input = TextInput(multiline=False)
        self.add_widget(self.recipient_input)

        self.add_widget(Label(text='Subject')) #subject textbox button
        self.subject_input = TextInput(multiline=False)
        self.add_widget(self.subject_input)

        self.add_widget(Label(text='Message'))  #message button / text box
        self.message_input = TextInput(multiline=True)
        self.add_widget(self.message_input)

        self.send_button = Button(text='Send Email') #send button
        self.send_button.bind(on_press=self.send_email_gui)
        self.add_widget(self.send_button)

        self.status_label = Label(text='', color=(1,0,0,1)) #red color for showing errors
        self.add_widget(self.status_label)

    def send_email_gui(self, instance):
        sender = email_address
        password = email_password
        recipient = self.recipient_input.text
        subject = self.subject_input.text
        message = self.message_input.text

        if not all([recipient, subject, message]):             #exception handling
            self.status_label.text = "All fields are required."
            return

        if not is_valid_email(recipient):
            self.status_label.text = "Invalid recipient email format"
            self.status_label.color = (1, 0, 0, 1)
            return

        success, feedback = send_email(sender, password, recipient, subject, message)
        self.status_label.text = feedback
        if success:
            self.status_label.color = (0, 0.6, 0, 1) #green if successful
        else:
            self.status_label.color = (1, 0, 0, 1)#red if not

class EmailApp(App):
    def build(self):
        self.title = "Email Sender App"
        return EmailForm()

if __name__ == '__main__': #main function
    EmailApp().run()



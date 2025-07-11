from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from Email_sender import send_email
from credentials import email_address, email_password
from Email_reader import get_recent_emails
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


class EmailForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=20, **kwargs)   #constructor

        self.add_widget(Label(text='Email Sender App', font_size=20, bold=True, size_hint_y=None, height=40))

        self.add_widget(Label(text='Recipient Email', font_size=16, size_hint_y=None, height=30)) #recipient button
        self.recipient_input = TextInput(multiline=False, font_size=14, size_hint_y=None, height=40)
        self.add_widget(self.recipient_input)

        self.add_widget(Label(text='Subject', font_size=16, size_hint_y=None, height=30)) #subject textbox button
        self.subject_input = TextInput(multiline=False, font_size=14, size_hint_y=None, height=40)
        self.add_widget(self.subject_input)

        self.add_widget(Label(text='Message', font_size=16, size_hint_y=None, height=30))  #message button / text box
        self.message_input = TextInput(multiline=True, font_size=14, size_hint_y=None, height=40)
        self.add_widget(self.message_input)

        self.send_button = Button(
            text='Send Email',
            background_color=(0.2, 0.6, 1, 1), #soft blue
            color=(1, 1, 1, 1), #white text
            font_size=16,
            size_hint=(1, None),
            height=50
        )
        self.send_button.bind(on_press=self.send_email_gui)

        self.add_widget(self.send_button)
        self.status_label = Label(text='', color=(1,0,0,1)) #red color for showing errors
        self.add_widget(self.status_label)

        self.clear_button = Button(
            text= 'Clear all fields',
            background_color=(0.5, 0.5, 0.5, 1), #gray color
            color = (1, 1, 1, 1), #white
            font_size = 16,
            size_hint = (1, None),
            height = 50
        )
        self.clear_button.bind(on_press=self.clear_fields)
        self.add_widget(self.clear_button)

        self.inbox_button = Button(
            text = 'View Inbox',
            background_color = (0.2, 0.8, 0.4, 1), #greenish
            color = (1, 1, 1, 1),
            font_size = 16,
            size_hint = (1, None),
            height = 50
        )
        self.inbox_button.bind(on_press=self.show_inbox)
        self.add_widget(self.inbox_button)


    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text=message, font_size=14))

        close_button = Button(text="Close", size_hint=(1, None), height=40, background_color=(0.8, 0, 0, 1), color=(1, 1, 1, 1))
        popup = Popup(title=title,
                      content=layout,
                      size_hint=(None, None),
                      size=(350, 200),
                      auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        layout.add_widget(close_button)
        popup.open()

    def send_email_gui(self, instance):
        sender = email_address
        password = email_password
        recipient = self.recipient_input.text
        subject = self.subject_input.text
        message = self.message_input.text

        if not all([recipient, subject, message]):
            self.show_popup("Missing fields", "All fields must be filled")
            return

        if not is_valid_email(recipient):
            self.show_popup("Invalid email", "The recipient email format is invalid")
            return

        success, feedback = send_email(sender, password, recipient, subject, message)
        self.status_label.text = feedback
        if success:
            self.status_label.color = (0, 0.6, 0, 1) #green if successful
        else:
            self.status_label.color = (1, 0, 0, 1)#red if not

    def clear_fields(self, instance):
        self.recipient_input.text = ''
        self.subject_input.text = ''
        self.message_input.text = ''
        self.status_label.text = ''

    def show_inbox(self, instance):
        try:
            # ... email creation and layout loop ...
            emails = get_recent_emails(limit=5)
            print(">>> Emails passed to GUI:", len(emails))  # DEBUG LINE

            layout = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
            layout.bind(minimum_height=layout.setter('height'))

            for email_data in emails:
                print(">>> Email content:", email_data)  # DEBUG LINE
                try:
                    # Clean and shortened the body preview
                    raw_body = email_data['body'].replace('\r', '').replace('\n', ' ').replace('\xa0', ' ')
                    short_body = raw_body[:200].strip() + "..."

                    snippet = f"[b]From:[/b] {email_data['from']}\n[b]Subject:[/b] {email_data['subject']}\n\n{short_body}"

                    label = Label(
                        text=snippet,
                        markup=True,  # to support [b][/b]
                        size_hint_y=None,
                        height=180,
                        font_size=14,
                        halign="left",
                        valign="top",
                        text_size=(380, None),
                        color=(1, 1, 1, 1)
                    )

                    layout.add_widget(label)
                except Exception as e:
                    print(">>> Error rendering email label:", e)

            scrollview = ScrollView(size_hint=(1, 1))
            scrollview.add_widget(layout)

            close_button = Button(
                text="Close",
                size_hint=(1, None),
                height=40,
                background_color=(0.8, 0, 0, 1),
                color=(1, 1, 1, 1)
            )

            box = BoxLayout(orientation='vertical')
            box.add_widget(scrollview)
            box.add_widget(close_button)

            popup = Popup(
                title="Inbox Preview",
                content=box,
                size_hint=(None, None),
                size=(450, 520),
                auto_dismiss=False
            )
            close_button.bind(on_press=popup.dismiss)
            popup.open()

        except Exception as e:
            print("Error rendering inbox", e)
            self.show_popup("Error", "Unable to render inbox:\n{e}")

class EmailApp(App):
    def build(self):
        self.title = "Email Sender App"
        return EmailForm()

if __name__ == '__main__': #main function
    EmailApp().run()



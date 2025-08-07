# import email and SMTP-related modules
import smtplib
from email.message import EmailMessage

# import os module to access .env file data
import os
from dotenv import load_dotenv

class CourseEmail:

    def __init__(self, recipient: str):
        # load environment variables
        load_dotenv()
        
        # SMTP configuration constants
        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_port = int(os.getenv("SMTP_PORT"))
        self.smtp_username = os.getenv("SMTP_USERNAME")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.sender_name = "GMU Course Checker"

        # user email
        self.recipient = recipient


    # Send an email. Returns true if successful and false if not
    def send_email(self, subject: str, body: str) -> bool:
        # create the message
        message = EmailMessage()
        message['Subject'] = subject
        message['From'] = self.smtp_username
        message['To'] = self.recipient
        message.set_content(body)

        try:
            with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port) as server:
                # login to the email provider
                server.login(self.smtp_username, self.smtp_password)

                # send email
                server.send_message(message)

        except Exception as e:
            # return false to indicate failed message
            return False
        
        # return true to indicate that message has been sent
        return True


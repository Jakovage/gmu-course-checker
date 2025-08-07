# import unit testing
import unittest

# import os module to access .env file data
from dotenv import load_dotenv

# import statements to access other classes
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import classes from project
from course_email import CourseEmail

class TestCourseEmail(unittest.TestCase):
    def setUp(self):
        # load enviornment variables
        load_dotenv()
        
        # create CourseEmail class
        self.email = CourseEmail(os.getenv("TEST_RECIPIENT_1"))

        # print env variables
        print(".env variables:")
        print("SMTP Host: " + self.email.smtp_host)
        print("SMTP Port: " + str(self.email.smtp_port))
        print("SMTP Username: " + self.email.smtp_username)
        print("SMTP Password: " + self.email.smtp_password)
        print("Recipient: " + self.email.recipient)

    def test_real_email(self):
        subject = "Unit testing email"
        body = "This is a test email from the test_real_email() method"
        self.assertTrue(self.email.send_email(subject, body))

if __name__ == "__main__":
    unittest.main()
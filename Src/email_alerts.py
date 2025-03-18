import os
import smtplib
import logging
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    filename="logs/email_alerts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class EmailAlerts:
    def __init__(self):
        """Initialize email alert system"""
        self.sender_email = os.getenv("EMAIL_SENDER")
        self.receiver_email = os.getenv("EMAIL_RECEIVER")
        self.email_password = os.getenv("EMAIL_PASSWORD")

    def send_alert(self, subject, message):
        """Send an email alert"""
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender_email, self.email_password)
                server.sendmail(self.sender_email, self.receiver_email, msg.as_string())

            logging.info(f"Email alert sent: {subject}")
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    alert = EmailAlerts()
    alert.send_alert("ADF Pipeline Failure", "One of the ADF pipelines has failed.")

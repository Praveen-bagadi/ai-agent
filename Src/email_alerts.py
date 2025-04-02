import smtplib
from email.mime.text import MIMEText
import logging

class EmailAlerts:
    def __init__(self, smtp_server: str, smtp_port: int, 
                 smtp_user: str, smtp_pass: str, receiver_email: str):
        """Initialize email alert system"""
        self.smtp_config = {
            'server': smtp_server,
            'port': smtp_port,
            'user': smtp_user,
            'password': smtp_pass
        }
        self.receiver = receiver_email
        self.logger = logging.getLogger(__name__)
        self.logger.info("EmailAlerts initialized")

    def send_alert(self, subject: str, message: str):
        """Send email notification"""
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.smtp_config['user']
        msg['To'] = self.receiver
        
        with smtplib.SMTP(self.smtp_config['server'], self.smtp_config['port']) as server:
            server.starttls()
            server.login(self.smtp_config['user'], self.smtp_config['password'])
            server.send_message(msg)
        self.logger.info(f"Sent alert: {subject}")
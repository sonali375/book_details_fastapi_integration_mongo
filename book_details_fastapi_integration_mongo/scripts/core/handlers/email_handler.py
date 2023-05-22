"""importing Email"""
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.core.schema.model import Email
from scripts.logging.logger import logger
from scripts.exceptions.exception_codes import EmailHandlerException


def send_email(body, email: Email):
    """Function to send email"""
    sender_email = os.environ.get("sender_email")
    sender_password = os.environ.get("sender_password")
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Total price of all the items"

    message.attach(MIMEText(body, "html"))

    try:
        logger.info("Handlers: send_email")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.send_message(message)

        server.quit()
        logger.info("send_email: Message sent successfully")
        return {"message": "Email sent"}
    except Exception as err:
        logger.error(EmailHandlerException.EX006.format(error=str(err)))
        return {"message": str(err)}

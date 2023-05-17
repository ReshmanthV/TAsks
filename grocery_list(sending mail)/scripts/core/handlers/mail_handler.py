import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scripts.config import Authentication
from scripts.core.handlers.gt_handlers import GTHandler
from scripts.schemas.gt_schema import Email
from scripts.db.mongo import CommonCollection

common = CommonCollection()


def send_mail(email: Email):
    # Set up the email details
    sender_email = Authentication.sender_mail
    sender_password = Authentication.sender_password
    receiver_email = email.receiver

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Grocery Amount"

    # Add the body to the email
    gt_handler = GTHandler()
    amount = gt_handler.cal_total()
    # message.attach(MIMEText(("Total amount : " + str(amount)), "plain"))
    get_list = common.find()
    final_list = json.dumps(get_list, indent=8)
    message.attach(MIMEText(final_list + "\nTotal Amount :" + str(amount), "plain"))
    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)

        # Close the connection
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}

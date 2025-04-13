# server.py
import smtplib
from email.message import EmailMessage
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os 



# Create an MCP server
mcp = FastMCP("Email sender")

load_dotenv()
@mcp.tool()
def send_email(subject,body,to_email):
    """
    Send an email using the configured Gmail account.

    Args:
        subject (str): The subject line of the email.
        body (str): The main content/body of the email.
        to_email (str): The recipient's email address.

    Returns:
        str: Confirmation message indicating the email was sent successfully,
             or an error message if the operation failed.
    """
    # Your Gmail credentials
    sender_email = os.getenv("Gmail")
    app_password = os.getenv("Google_password")  # Use App Password from Google

    # Create the email
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        return ("Email sent successfully!")
    except Exception as e:
        return ("Error:", e)
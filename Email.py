import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === EMAIL CONFIG ===
SENDER_EMAIL = "pintu@lal10.com"
SENDER_PASSWORD = "hhjo szeq lsei ihee"  # Use Gmail App Password
RECEIVER_EMAIL = "kumar.pintujha76@gmail.com"

# === Create the Email Message ===
subject = "Welcome to Our Website"
body = """
Hi there,<br><br>
Welcome to our website! We're glad to have you on board.<br><br>
Best regards,<br>
Your Website Team
"""

msg = MIMEMultipart("alternative")
msg["Subject"] = subject
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL

msg.attach(MIMEText(body, "html"))

# === Send the Email ===
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print("Failed to send email:", str(e))

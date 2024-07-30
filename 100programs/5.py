import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sender's email address
from_addr = 'ENTER_SENDERS_MAILID'

# Read the CSV file containing emails and names
data = pd.read_csv("abc.csv")  # Enter the path of the CSV file
to_addr = data['email'].tolist()  # Column name containing email addresses
name = data['name'].tolist()  # Column name containing names

# Number of recipients
l = len(name)

# Your email credentials
email = "YOUR_EMAIL"  # Enter your email ID here
password = "YOUR_PASSWORD"  # Enter your email password here

# Loop through each recipient and send the email
for i in range(l):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr[i]
    msg['Subject'] = 'Just to Check'

    # Body of the email (HTML content)
    body = f"""
    <html>
    <body>
        <p>Hi {name[i]},<br><br>
        Enter your content here<br><br>
        Best regards,<br>
        Your Name
        </p>
    </body>
    </html>
    """

    # Attach the HTML content to the email
    msg.attach(MIMEText(body, 'html'))

    # Connect to the Gmail SMTP server and send the email
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)
    text = msg.as_string()
    mail.sendmail(from_addr, to_addr[i], text)
    mail.quit()

print("Emails have been sent successfully.")

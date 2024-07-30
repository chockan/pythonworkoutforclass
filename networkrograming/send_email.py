import email.message
import email.policy
import email.utils
import sys

text = """Welcome to TutorialsPoint - Simple Easy Learning"""

message = email.message.EmailMessage(email.policy.SMTP)
message['To'] = 'chockansamy@gmail.com'
message['From'] = 'Learn '
message['Subject'] = 'A mail To you'
message['Date'] = email.utils.formatdate(localtime=True)
message['Message-ID'] = email.utils.make_msgid()
message.set_content(text)
sys.stdout.buffer.write(message.as_bytes())
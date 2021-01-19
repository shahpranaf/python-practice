import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text()) 
email = EmailMessage()
email['from'] = 'Pranav Shah'
email['to'] = 'shahpranaf@gmail.com'
email['subject'] = 'Congratulations for your wedding'

email.set_content(html.substitute({'name': 'Pranav'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@gmail.com', 'password')
    smtp.send_message(email)
    print("All good..")

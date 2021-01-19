import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Pranav Shah'
email['to'] = 'shahpranaf@gmail.com'
email['subject'] = 'Congratulations for your wedding'

email.set_content("Congratulations !! its Celebration pava")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@gmail.com', 'password')
    smtp.send_message(email)
    print("All good..")

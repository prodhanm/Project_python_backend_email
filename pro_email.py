import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values
from string import Template
from pathlib import Path
from email_addr import *

config = dotenv_values(".env")

#html = Template(Path("index.html").read_text())
email = EmailMessage()

email['from'] = email_from
email['to'] = email_to
email['cc'] = email_cc

email['bcc'] = [mail for mail in email_bcc]

email['subject'] = 'Good Day!!'

#email.set_content(html.substitute(name="Mufassa"), 'html')
email.set_content('Test')

with smtplib.SMTP(host=config["HOST"], \
                  port=config["PORT"]) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config['USERNAME'], config['PASSWORD'])
    smtp.send_message(email)
    print('done')
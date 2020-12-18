
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
# from django.core.mail import send_mail

# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
#
# message = Mail(
#     from_email='priyanshbordia1@gmail.com',
#     to_emails='priyanshbordia2@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

# send_mail(
# 'Password Reset Link',
# 'Hello.!, there below is the link where you can reset your password.',
# '19ucs257@lnmiit.ac.in',
# ['19uec117@lnmiit.ac.in'],
# fail_silently=False,
# )

# send_mail('Password Reset Link', 'Hello.!, there below is the link where you can reset your password.', '19ucs257@lnmiit.ac.in', ['priyanshbordia2@gmail.com'], fail_silently=False,)


import smtplib

# username = '19'
# password = 'I9FI97H7'
sender = '19ucs257@lnmiit.ac.in'
receivers = ['19uec117@lnmiit.ac.in']

message = """From: From Person <19ucs257@lnmiit.ac.in>
To: To Person <19uec117@lnmiit.ac.in>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.starttls()
    smtpObj.login(username,password)
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")

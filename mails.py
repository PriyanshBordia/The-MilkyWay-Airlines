
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='priyanshbordia1@gmail.com',
    to_emails='priyanshbordia2@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

# from django.core.mail import send_mail
# send_mail('Password Reset Link', 'Hello.!, there below is the link where you can reset your password.', '19ucs257@lnmiit.ac.in', ['priyanshbordia2@gmail.com'], fail_silently=False,)

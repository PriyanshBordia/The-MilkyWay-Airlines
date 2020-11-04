# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
#
#
# message = Mail(
#     from_email='amdin@milkywayairlines.org',
#     to_emails='priyanshbordia2@gmail.com',
#     subject='Hello.!',
#     html_content='<strong>having fuz</strong>',
# )
#
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)

import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
to_email = To("test@example.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

# from django.core.mail import send_mail
# send_mail('Password Reset Link', 'Hello.!, there below is the link where you can reset your password.', '19ucs257@lnmiit.ac.in', ['priyanshbordia2@gmail.com'], fail_silently=False,)

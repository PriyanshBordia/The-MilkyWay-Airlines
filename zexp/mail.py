# # Import smtplib for the actual sending function
# import smtplib
#
# # Import the email modules we'll need
# from email.message import EmailMessage
#
# # Open the plain text file whose name is in textfile for reading.
# # with open(textfile) as fp:
# #     # Create a text/plain message
# msg = EmailMessage()
# msg.set_content('Hello, World.!')
#
# me = '19ucs257@lnmiit.ac.in'
# you = '19uec117@lnmiit.ac.in'
# msg['Subject'] = f'The contents of mail'
# msg['From'] = me
# msg['To'] = you
#
# # Send the message via our own SMTP server.
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.ehlo()
# s.starttls()
# s.ehlo()
# s.login('myname@gmail.com','mypass')
# s.send_message(msg)
# s.quit()

import yagmail
yag = yagmail.SMTP('priyanshbordia2@gmail.com')
yag.send('19uec117@lnmiit.ac.in', subject = None, contents = 'Hello')

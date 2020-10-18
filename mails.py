from django.core.mail import send_mail

send_mail('Password Reset Link', 'Hello.!, there below is the link where you can reset your password.', '19ucs257@lnmiit.ac.in', ['priyanshbordia2@gmail.com'], fail_silently=False,)

from api.models import EmailModel, MessageModel
from api.tasks import send_email_background


def save_email_db(email: str):
    """
    Saves email to Email Table.
    email: str -> recieve email from request.
    """
    EmailModel.objects.create(email=email)


def send_email_newsletter(sub, message):
    """
    Send emails to the list of subscribers.
    sub -> subject of email
    message -> body/message of email
    """
    from django.core.mail import send_mail

    print("Hello from services.py > send_email_newsletter")

    emails = EmailModel.objects.all()
    users: list[str] = [x.email for x in emails]

    for user in users:
        send_mail(
            subject=sub,
            message=message,
            recipient_list=[user],
            from_email="bitsj2@gmail.com",
        )

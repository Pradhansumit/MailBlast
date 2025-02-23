from api.models import EmailModel


def save_email_db(email: str):
    """
    Saves email to Email Table.
    email: str -> recieve email from request.
    """
    EmailModel.objects.create(email=email)

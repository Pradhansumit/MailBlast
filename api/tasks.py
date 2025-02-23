import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def send_email_background(title, desc):
    """
    Sends emails in background.
    title: str -> Subject of email
    desc: str -> body/message of email
    """
    logger.info("-> Background task initiated.")
    from api.services import send_email_newsletter

    try:
        send_email_newsletter(sub=title, message=desc)
        logger.info("Email sent successfully.")

    except Exception as e:
        logger.error(f"Error sending email: {e}")
        raise Exception

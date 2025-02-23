import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import MessageModel
from api.tasks import send_email_background

logger = logging.getLogger(__name__)


@receiver(signal=post_save, sender=MessageModel)
def notify_messagemodel_on_save(sender, instance, created, **kwargs):
    if created:
        title = instance.title
        description = instance.description

        logger.info("Sending request to celery.")

        send_email_background.delay_on_commit(title, description)

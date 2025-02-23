from django.db import models


# Create your models here.
class EmailModel(models.Model):
    """
    For storing email of users that are subscribing to the newsletter.
    """

    email = models.EmailField()

    def __str__(self) -> str:
        return self.email


class MessageModel(models.Model):
    """
    Newsletter content that will be sent to users.
    """

    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

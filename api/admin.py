from django.contrib import admin

from api.models import EmailModel, MessageModel


@admin.register(EmailModel)
class EmailAdmin(admin.ModelAdmin):
    fields = ["email"]


@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    fields = ["title", "description"]

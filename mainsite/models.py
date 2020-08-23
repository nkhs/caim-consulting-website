from datetime import datetime

from django.db import models
from django.conf import settings


class Service(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}: {self.subject}"


class Message(models.Model):
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)
    offset = models.BigIntegerField(editable=False)
    by_admin = models.BooleanField(default=False)
    message_text = models.TextField()

    def save(self, *args, **kwargs):
        d = datetime.now()
        self.offset = d.strftime("%Y%m%d%H%M%S")
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        if self.by_admin:
            return f"ADMIN: {self.message_text}"
        return f"{self.chat}: {self.message_text}"

    class Meta:
        unique_together = (("chat", "offset"),)

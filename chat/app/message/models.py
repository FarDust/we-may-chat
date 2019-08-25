from django.db import models
from django.contrib.sessions.models import Session

# Create your models here.

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    session = models.ForeignKey(Session,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True
                                )
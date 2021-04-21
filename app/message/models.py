from django.db import models

# Create your models here.


class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    nickname = models.CharField(max_length=50, default='', editable=False)

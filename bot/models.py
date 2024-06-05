from django.db import models

class ChatMessage(models.Model):
    user = models.CharField(max_length=1000)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

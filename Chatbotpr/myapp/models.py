from django.db import models
# Create your models here.

class ChatHistory(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add= True)

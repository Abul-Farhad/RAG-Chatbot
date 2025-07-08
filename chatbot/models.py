from django.db import models

class ChatMemory(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    state_json = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ChatMemory for {self.session_id}"

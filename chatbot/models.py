from django.db import models

class ChatMemory(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    state_json = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ChatMemory for {self.session_id}"


class Product(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    reviews = models.JSONField()

    def __str__(self):
        return f"{self.brand} {self.model}"

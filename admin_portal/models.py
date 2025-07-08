from django.db import models

# Create your models here.
class Issue(models.Model):
    issued_by = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='issues')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
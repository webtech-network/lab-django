from django.db import models

# Create your models here
class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    due_to = models.DateTimeField(blank=True, auto_now=False)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.name


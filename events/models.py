from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    description = models.DateTimeField('date published')
    link = models.CharField(max_length=200)
    submitted_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




from django.db import models
from django.contrib.auth.models import User

class Topic (models.Model):
    """Topic which chose user"""
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry (models.Model):
    """Information about chosen topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."




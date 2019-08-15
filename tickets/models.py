from django.db import models
from django.contrib.auth.models import User
from .choices import *
# Create your models here.


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3)
    attachment = models.FileField(upload_to='attachment/', blank=True, null=True)

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return self.content


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content


class Response(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    respond = models.TextField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.respond





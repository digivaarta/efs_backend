from pyexpat import model
from random import choice
from statistics import mode
from django.db import models
from django_extensions.db.fields import RandomCharField

# Create your models here.

class SupportChoices(models.TextChoices):
    OPEN = "open","Open"
    CLOSED = "closed","Closed"

    




class Ticket(models.Model):
    user = models.ForeignKey("account.User",on_delete=models.CASCADE,related_name="user_ticket")
    subject = models.CharField(max_length=100)
    ticket_no = RandomCharField(length=12, lowercase=True, include_digits=False)
    status = models.CharField(max_length=100,choices=SupportChoices.choices,default=SupportChoices.OPEN)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Support(models.Model):
    sender = models.ForeignKey("account.User",on_delete=models.CASCADE,related_name="user_support")
    ticket = models.ForeignKey("support.Ticket",on_delete=models.CASCADE,related_name="ticket_conversation")
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
from django.contrib.auth.models import User
from django.db import models


MODE_CHOICES = (
    ('BID', 'Bidding'),
    ('ASK', 'Asking')
)


class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()


class Auction(models.Model):
    project = models.ForeignKey(Project)
    url = models.URLField()
    summary = models.CharField(max_length=200)


class Bid(models.Model):
    auction = models.ForeignKey(Auction)
    user = models.ForeignKey(User)
    mode = models.CharField(max_length=3,
                            choices=MODE_CHOICES,
                            default='BID')
    amount = models.DecimalField(max_digits=8,
                                 decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

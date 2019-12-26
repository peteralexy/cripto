from django.db import models

# Create your models here.
class Voter(models.Model):
    voter_name = models.CharField(max_length=50)
    voter_age = models.IntegerField(null=True)
    voter_city = models.CharField(max_length=50)
    voter_county = models.CharField(max_length=50)
    voter_address = models.CharField(max_length=100)
    voter_vote = models.CharField(max_length=50)
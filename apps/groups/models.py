from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    creator = models.ForeignKey(User, related_name='creator')
    members = models.ManyToManyField(User, related_name='member')

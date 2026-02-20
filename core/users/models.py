from django.db import models
from django.db.models import Q

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

   # class Meta:
    #    constraints = [models.CheckConstraint(condition=Q(age__gte=18), name="age_must_be_18_or_older")]

    def __str__(self):
        return self.username

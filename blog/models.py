from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    by = models.ForeignKey(User)
    title = models.CharField(max_length=127)
    content = models.TextField()
    publishing_date = models.DateField()
    hidden = models.BooleanField()

    class Meta:
        ordering = ('-publishing_date',)


class Tag(models.Model):
    name = models.CharField(max_length=31)

    class Meta:
        ordering = ('name',)

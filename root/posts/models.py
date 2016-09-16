from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    STATUS_CHOICES = (('A', 'Approved'),('I','In Progress'),('D','Declined'), ('R','Under Review'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='R')
    status_desc = models.TextField()

    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)

class Follows(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    followed_on = models.DateTimeField()

class Vote(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
    VOTE_CHOICES = (('U', 'Up vote'),('D','Down vote'))
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES)

class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    comment = models.TextField()
    posted_on = models.DateTimeField()
    updated_on = models.DateTimeField()

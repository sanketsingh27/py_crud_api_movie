# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Movie Modal
class Movie(models.Model):
    name = models.CharField(max_length =200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return '%s %s' % (self.name, self.body)
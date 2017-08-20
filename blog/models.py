# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, null=True)
    body = models.TextField()
    author = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.title

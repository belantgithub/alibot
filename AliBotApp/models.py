# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TelegramUsers(models.Model):
    username = models.CharField(max_length=50)


class Channels(models.Model):
    owner = models.ForeignKey(TelegramUsers)
    channel_name = models.CharField(max_length=50)


class Analysis(models.Model):
    author = models.ForeignKey(TelegramUsers)
    channel = models.ForeignKey(Channels)
    analysis = models.TextField()

# Create your models here.

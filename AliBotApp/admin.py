# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TelegramUsers, Analysis, Channels

admin.site.register(TelegramUsers)
admin.site.register(Analysis)
admin.site.register(Channels)

# Register your models here.

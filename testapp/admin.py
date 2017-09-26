# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test

class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'test']

admin.site.register(Test, TestAdmin)

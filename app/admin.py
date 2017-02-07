#! -*- coding=utf-8 -*-
from django.contrib import admin
from app.models import BasicData

@admin.register(BasicData)
class BasicDataAdmin(admin.ModelAdmin):
    list_display=('our_name',)

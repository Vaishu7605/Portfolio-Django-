from django.contrib import admin
from .models import *


@admin.register(message)
class messageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Your_Name','Your_Email','Subject','Message')
# Register your models here.

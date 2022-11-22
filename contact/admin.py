from django.contrib import admin
from .models import *


class AdminContact(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'message')


admin.site.register(Contact, AdminContact)

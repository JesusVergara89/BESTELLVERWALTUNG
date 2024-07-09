from django.contrib import admin
from .models import services

class admin_services(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(services,admin_services)

from django.contrib import admin
from .models import Categories, Post

class admin_post(admin.ModelAdmin):
    readonly_fields=('created','updated')

class admin_category(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categories,admin_category)
admin.site.register(Post,admin_post)


from django.contrib import admin
from .models import blogs


class Blog_admin (admin.ModelAdmin):
    list_display = ('title', 'text', 'author')


admin.site.register(blogs, Blog_admin)

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'modified_time', 'category', 'author']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

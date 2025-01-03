from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'auther', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'auther']

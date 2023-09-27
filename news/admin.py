from django.contrib import admin
from .models import Category, Post
from django.utils.html import format_html

# Register your models here.
admin.site.site_header = "NEWS ADMIN"
admin.site.site_title = "NEWS PORTAL"
admin.site.index_title = "API List"

admin.site.register(Category)
admin.site.register(Post)
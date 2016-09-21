from django.contrib import admin

# Register your models here.
from .models import Category, Post, Vote, Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Vote)
admin.site.register(Comment)

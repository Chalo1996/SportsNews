from django.contrib import admin
from blog.models import Post, Comment, BlogUser

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(BlogUser)
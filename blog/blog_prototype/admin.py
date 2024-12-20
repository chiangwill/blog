from django.contrib import admin

from blog_prototype.models.blog import Comment, Post
from blog_prototype.models.user import User

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Post)

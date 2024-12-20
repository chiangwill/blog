from django.db import models


class Post(models.Model):

    user = models.ForeignKey('blog_prototype.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    user = models.ForeignKey('blog_prototype.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('blog_prototype.Post', related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.title}'s comment"

from django.db import models
from django.contrib.auth.models import User

class BlogUtama(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    line = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='blog_posts/')
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    description = models.TextField()
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='blog_posts_likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class RelatedPost(models.Model):
    title = models.CharField(max_length=255)
    blog_post = models.ForeignKey(BlogPost, related_name='related_posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

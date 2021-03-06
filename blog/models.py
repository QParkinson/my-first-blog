from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 180)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    post_id = models.IntegerField(default=0)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    comment_id = models.IntegerField(default=0)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
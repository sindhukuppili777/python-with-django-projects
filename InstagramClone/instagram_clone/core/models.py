from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.caption


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
   

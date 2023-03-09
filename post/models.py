from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    # post 모델에 tags 필드 추가
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()




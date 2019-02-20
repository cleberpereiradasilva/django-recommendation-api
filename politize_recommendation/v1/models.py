from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    tags = models.ManyToManyField(
        to='v1.Tag',
        related_name='posts',
        verbose_name="tags",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="nome",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="criado em",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="última modificação"
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="nome",
    )

    def __str__(self):
        return self.name


class PostView(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='post_views')

    post = models.ForeignKey(
        to='v1.Post',
        on_delete=models.CASCADE,
        related_name='post_views',
    )    
    viewed_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="visualizado em",
    )

    def __str__(self):
        return '{0}-{1}'.format(self.post, self.viewed_at)


# class User(models.Model):
#     views = models.ManyToManyField(
#         to='v1.Post',
#         through='v1.PostView',
#         related_name='user_views',
#     )  

    
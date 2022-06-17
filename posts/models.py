from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'created datetime', blank=True, auto_now_add=True
    )
    image= CloudinaryField(
        'image', blank=True, null = True, db_index=True
    )
    like = models.IntegerField(
        'likes', blank=True, null = True, db_index=True, default=0
    )
        
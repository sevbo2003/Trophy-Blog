from distutils.command.upload import upload
from statistics import mode
from django import views
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30)
    category_image = models.ImageField(upload_to='category_images')

    def __str__(self) -> str:
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=210)
    # slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    active = models.BooleanField(default=True)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    images = models.ImageField(upload_to='post_images')
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ('created_at', )

    def __str__(self) -> str:
        return self.title

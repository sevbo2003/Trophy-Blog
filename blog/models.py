from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    category = models.CharField(max_length=30)
    category_image = models.ImageField(upload_to='category_images')

    def __str__(self) -> str:
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=210)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = RichTextField()
    active = models.BooleanField(default=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    images = models.ImageField(upload_to='post_images')
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.text[:10] + " | " + str(len(self.text))

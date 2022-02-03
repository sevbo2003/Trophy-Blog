# Generated by Django 4.0.2 on 2022-02-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('category_image', models.ImageField(upload_to='category_images')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=210)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('comments', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('images', models.ImageField(upload_to='post_images')),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]

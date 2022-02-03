from django.contrib import admin

# Register your models here.
from .models import Post, Category


admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'active','views')
    list_filter = ('updated_at', 'active', 'category', 'views')
    prepopulated_fields = {'slug': ('title',)}
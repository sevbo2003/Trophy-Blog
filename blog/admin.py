from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comments


admin.site.register(Category)
admin.site.register(Comments)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'active','view_count')
    list_filter = ('updated_at', 'active', 'category', 'view_count')
    prepopulated_fields = {'slug': ('title',)}
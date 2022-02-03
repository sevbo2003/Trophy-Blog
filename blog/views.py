from django.db.models import Count
from django.shortcuts import render
from .models import Category, Post

def get_category_count():
    queryset = Post.objects.values('category__category').annotate(Count('category'))
    return queryset

# Create your views here.
def post_list(request):
    category_count = get_category_count()
    print(category_count)
    posts = Post.objects.filter(active=True)
    categories = Category.objects.all()
    context = {'posts': posts, 'categories': categories, 'category_count': category_count}
    return render(request, 'home.html', context)
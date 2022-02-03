from multiprocessing import context
from tokenize import Triple
from django.shortcuts import render
from .models import Category, Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(active=True)
    categories = Category.objects.all()
    context = {'posts': posts, 'categories': categories}
    return render(request, 'home.html', context)

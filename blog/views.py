from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Category, Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(active=True)
    paginator = Paginator(posts, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    context = {'posts': paginated_queryset, 'categories': categories, 'page_request_var': page_request_var}
    return render(request, 'home.html', context)
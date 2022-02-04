from turtle import pos
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Comments, Post
from .forms import CommentForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(active=True)
    paginator = Paginator(posts, 3)
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



def post_detail(request, slug):
    form = CommentForm(request.POST)
    post = get_object_or_404(Post, slug = slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            name = request.POST.get('name')
            text = request.POST.get('text')
            comment = Comments.objects.create(post=post, text=text, name=name)
            comment.save()
            return redirect(post.slug)
        else:
            form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'form': form})

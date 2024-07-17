from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def index(request):
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category).order_by('-publication_date')

    date_filter = request.GET.get('date')
    if date_filter:
        posts = posts.filter(publication_date__date=date_filter)

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/category_detail.html', {
        'category': category,
        'page_obj': page_obj,
        'date_filter': date_filter,
    })


def post_detail(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    categories = post.categories.all()
    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Categories', 'url': '/categories/'},
    ]
    for category in categories:
        breadcrumbs.append({'name': category.name, 'url': f'/category/{category.slug}/'})
    breadcrumbs.append({'name': post.title, 'url': f'/news/{category_slug}/{post_slug}/'})
    return render(request, 'blog/post_detail.html', {'post': post, 'breadcrumbs': breadcrumbs})

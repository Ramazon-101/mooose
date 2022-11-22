from django.shortcuts import render, redirect
from .models import *
from contact.models import Subscribe
from .forms import CommentForm


def home(request):
    posts = Article.objects.filter(is_published=True)
    author = About.objects.all()
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    context = {
        'author': author,
        'posts': posts,
        'email': email,
    }
    return render(request, 'website/index.html', context)


def about(request):
    person = Article.objects.all()
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    context = {
        'person': person,
        'email': email,
    }
    return render(request, 'website/about.html', context)


def articles(request):
    posts = Article.objects.all().order_by('-id')
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    context = {
        'posts': posts,
        'email': email,

    }
    return render(request, 'website/blog.html', context)


def blog_detail(request, slug):
    post = Article.objects.get(slug=slug)
    author = About.objects.all()
    email = request.POST.get('email')
    if request.method == 'POST':
        Subscribe.objects.create(email=email)
    comments = Comment.objects.filter(article__slug__exact=slug).order_by('-id')
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = post
        comment.user = request.user
        comment.save()
        return redirect(f'blog_detail/{post.slug}#comment')
    context = {
        'author': author,
        'post': post,
        'email': email,
        'comments': comments,
        'form': form,
    }
    return render(request, 'website/blog-single.html', context)


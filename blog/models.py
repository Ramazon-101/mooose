from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    user_pr = models.ForeignKey(Profession, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/')
    subtitle = RichTextField()

    def __str__(self):
        return self.username


class Article(models.Model):
    # author = models.ForeignKey(About, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    content = RichTextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    web = models.URLField(null=True, blank=True)
    img = models.ImageField(upload_to='comment/')
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='blog/images/')
    preview_image = models.ImageField(upload_to='blog/images/')
    summary = models.TextField()
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

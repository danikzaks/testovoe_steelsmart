from django.db import models
from django.core.files.base import ContentFile
from PIL import Image as PilImage
import io


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='images/')
    preview_image = models.ImageField(upload_to='images/', null=True, blank=True)
    summary = models.TextField()
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        # Resize images
        if self.main_image:
            self.main_image = self.resize_image(self.main_image, (300, 200))

        if self.preview_image:
            self.preview_image = self.resize_image(self.preview_image,
                                                   (150, 100))

        super().save(*args, **kwargs)

    def resize_image(self, image_field, size):
        image = PilImage.open(image_field)

        if image.mode == 'RGBA':
            image = image.convert('RGB')

        image.thumbnail(size, PilImage.LANCZOS)
        img_io = io.BytesIO()
        image.save(img_io, format='JPEG', quality=85)
        img_file = ContentFile(img_io.getvalue(), name=image_field.name)
        return img_file

    def __str__(self):
        return self.title

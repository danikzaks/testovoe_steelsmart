from django.db import models
from django.core.files.base import ContentFile
from PIL import Image as PilImage
import io
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    main_image = models.ImageField(upload_to='images/', verbose_name='Основное изображение')
    preview_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение превью')
    summary = models.TextField(verbose_name='Аннотация')
    content = RichTextField(verbose_name='Содержимое')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    categories = models.ManyToManyField(Category, verbose_name='Категории')

    def save(self, *args, **kwargs):
        # Resize images (сохранение изображений)
        if self.main_image:
            self.main_image = self.resize_image(self.main_image, (300, 200))

        if self.preview_image:
            self.preview_image = self.resize_image(self.preview_image, (150, 100))

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

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

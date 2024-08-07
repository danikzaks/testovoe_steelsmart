# Generated by Django 5.0.7 on 2024-07-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("main_image", models.ImageField(upload_to="images/")),
                ("preview_image", models.ImageField(upload_to="images/")),
                ("summary", models.TextField()),
                ("content", models.TextField()),
                ("publication_date", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(unique=True)),
                ("categories", models.ManyToManyField(to="blog.category")),
            ],
        ),
    ]

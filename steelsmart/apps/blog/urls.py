from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.categories, name="categories"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path(
        "news/<slug:category_slug>/<slug:post_slug>/",
        views.post_detail,
        name="post_detail",
    ),
]

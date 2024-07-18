from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category
from ckeditor.widgets import CKEditorWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "content": CKEditorWidget(),
        }


class ImagePreviewAdminMixin:
    def image_preview(self, obj):
        if obj.preview_image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px;" />',
                obj.preview_image.url,
            )
        else:
            return "(No image)"

    image_preview.short_description = "Превью"
    image_preview.allow_tags = True


class PostAdmin(ImagePreviewAdminMixin, admin.ModelAdmin):
    form = PostAdminForm
    list_display = ("title", "publication_date", "get_categories", "image_preview")
    list_filter = ("publication_date", "categories")
    search_fields = ("title", "summary", "content")
    filter_horizontal = ("categories",)
    prepopulated_fields = {"slug": ("title",)}

    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])

    get_categories.short_description = "Категории"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

admin.site.site_header = "Административная панель блога"
admin.site.site_title = "Админка блога"
admin.site.index_title = "Добро пожаловать в админку блога"

from django.contrib import admin
from .models import Post, Category
from ckeditor.widgets import CKEditorWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'publication_date', 'get_categories')
    list_filter = ('publication_date', 'categories')
    search_fields = ('title', 'summary', 'content')

    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])

    get_categories.short_description = 'Categories'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

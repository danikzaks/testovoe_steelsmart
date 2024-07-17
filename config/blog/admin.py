from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'publication_date')
    list_filter = ('categories', 'publication_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'publication_date'
    filter_horizontal = ('categories',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

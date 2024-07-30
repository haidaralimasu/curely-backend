from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Category


class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ("slug",)
    list_display = ("id", "title", "category", "date_created")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_per_page = 25
    summernote_fields = ("content",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)

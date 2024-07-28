from django.contrib import admin
from .models import NewsLetter


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "is_subscribed")
    list_display_links = ("id", "email", "is_subscribed")
    search_fields = (
        "id",
        "email",
    )
    list_per_page = 25


admin.site.register(NewsLetter, NewsLetterAdmin)

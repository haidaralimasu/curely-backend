from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name")
    list_display_links = ("id", "user_name")
    search_fields = (
        "id",
        "user_name",
    )
    list_per_page = 25


admin.site.register(Testimonial, TestimonialAdmin)

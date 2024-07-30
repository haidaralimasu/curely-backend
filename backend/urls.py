from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static

# Admin page customizations
admin.site.site_header = "Curely Admin"
admin.site.site_title = "Curely Admin Dashboard"
admin.site.index_title = "Curely Admin Dashboard"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),  # Django rest framework auth
    path("api/v1/summernote/", include("django_summernote.urls")),  # Summer note
    path(
        "favicon.ico", lambda _: redirect("static/favicon.png", permanent=True)
    ),  # Favicon
    path("api/v1/admin/", admin.site.urls),  # Admin site
    path("api/v1/newsletter/", include("newsletter.urls")),  # Newsletter urls
    path("api/v1/blog/", include("blog.urls")), # Blog urls
    path("api/v1/testimonials/", include("testimonials.urls")), # Testimonials urls
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # Media urls

from django.db import models
from django.utils import timezone

now = timezone.now()


class Testimonial(models.Model):
    user_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="photos/testimonials/")
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user_name

from django.db import models
from django.utils import timezone

now = timezone.now()


class NewsLetter(models.Model):
    email = models.EmailField(max_length=100)
    is_subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.email

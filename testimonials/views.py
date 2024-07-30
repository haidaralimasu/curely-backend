from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialListView(ListAPIView):
    queryset = Testimonial.objects.order_by("-created_at")
    serializer_class = TestimonialSerializer
    lookup_field = "user_name"
    permission_classes = (permissions.AllowAny,)

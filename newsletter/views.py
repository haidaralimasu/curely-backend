from .serializers import NewsLetterSerializer
from rest_framework import generics, permissions
from .models import NewsLetter


class NewsLetterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

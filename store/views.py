from rest_framework import generics

from store.models import Book
from store.serializers import BookSerializer


class BooksListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.select_related('author').values('name', 'author__name')

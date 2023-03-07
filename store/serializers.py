from rest_framework import serializers

from store.models import Book


class BookSerializer(serializers.ModelSerializer):
    author__name = serializers.CharField()

    class Meta:
        model = Book
        fields = ('name', 'author__name', )

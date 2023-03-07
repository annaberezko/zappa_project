from django.urls import path

from store.views import BooksListAPIView


urlpatterns = [
    path('', BooksListAPIView.as_view(), name='course-list'),
    ]

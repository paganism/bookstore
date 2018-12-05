from django.urls import path

from .views import *

urlpatterns = [
    path('', BookListView.as_view(), name='store' ),
    path('book/<pk>', BookDetailView.as_view(), name='book-detail'),
    path('author/<pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('catalog/', catalog_view, name='catalog'),
]
from django.urls import path

from .views import *

urlpatterns = [
    path('store/', BookListView.as_view(), name='books' ),
    path('book/<pk>', BookDetailView.as_view(), name='book-detail'),
]
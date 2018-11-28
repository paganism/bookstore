from django.urls import path

from .views import *

urlpatterns = [
    path('books/', BookListView.as_view(), name='books' ),
]
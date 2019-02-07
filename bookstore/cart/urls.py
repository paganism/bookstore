from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartDetail, name='CartDetail'),
    path('remove/<product_id>', views.CartRemove, name='CartRemove'),
    path('add/<product_id>', views.CartAdd, name='CartAdd'),
    
]



# path('', BookListView.as_view(), name='store'),
#     path('book/<pk>', BookDetailView.as_view(), name='book-detail'),
#     path('author/<pk>', AuthorDetailView.as_view(), name='author-detail'),
#     path('catalog/', catalog_view, name='catalog'),
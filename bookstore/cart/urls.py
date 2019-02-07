from django.urls import path
from . import views

urlpatterns = [
    url('remove/<product_id>', views.CartRemove, name='CartRemove'),
    url('add/<product_id>', views.CartAdd, name='CartAdd'),
    url('', views.CartDetail, name='CartDetail'),
]

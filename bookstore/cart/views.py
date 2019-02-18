from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book, GenreGroups
from .cart import Cart
from .forms import CartAddProductForm
from store.views import GENRE_GROUPS_LIST


@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=product, qty=cd['quantity'],
                                update_quantity=cd['update'])
    return redirect('CartDetail')

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, title=product_id)
    cart.remove(product)
    return redirect('CartDetail')

def CartDetail(request):
    cart = Cart(request)
    genregroups_list = GENRE_GROUPS_LIST
    for item in cart: 
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={ 
                                            'quantity': item['qty'], 
                                            'update': True })
    return render(request, 'cart/detail.html', {'cart': cart, 'genregroups_list': genregroups_list})

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book
from .cart import Cart
from .forms import CartAddProductForm


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
    product = get_object_or_404(Book, id=product_id)
    print('PRODUCT IS: {}'.format(product))
    cart.remove(product)
    return redirect('CartDetail')

def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
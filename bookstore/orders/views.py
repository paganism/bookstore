from django.shortcuts import render

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from . tasks import OrderCreated


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                print(item)
                OrderItem.objects.create(order=order, product=item['book'],
                                         price=item['price'],
                                         quantity=item['qty'])
            cart.clear()
            OrderCreated.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


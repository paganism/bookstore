from decimal import Decimal
from django.conf import settings
from store.models import Book


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if bot cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, book, qty=1, update_qty=False):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'qty': 0,
                                    'price': str(book.price)}
        if update_quantity:
            self.cart[book_id]['qty'] = qty
        else:
            self.cart[book_id]['qty'] += qty
        self.save()
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart['book_id']
            self.save()
    
    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book
    
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['total_price'])
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] fot item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

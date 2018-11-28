from django.shortcuts import render
from django.views import generic

from .models import Book, Author


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is some data'
        return context

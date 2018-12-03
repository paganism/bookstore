from django.shortcuts import render
from django.views import generic

from .models import Book, Author, GenreGroups


# Create your views here.
class BookListView(generic.ListView):
    model = Book, GenreGroups
    paginate_by = 20
    template_name = 'store/book_list.html'

    def get_queryset(self):
        book_list = Book.objects.all()
        return book_list
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
        print(context)
        return context


class BookDetailView(generic.DetailView):
    model = Book
    
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
        print(context)
        return context

class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
        print(context)
        return context

class CatalogView(generic.ListView):
    model = GenreGroups
    template_name = 'store/catalog.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
        context['book_list'] = book_list = Book.objects.all()
        return context


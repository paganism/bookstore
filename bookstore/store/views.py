from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Max, Min

from .models import Book, Author, GenreGroups, Genre


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
    # model = Book
    template_name = 'store/catalog.html'
    # context_object_name = 'book_list'
    paginate_by = 8

    def get_queryset(self):
        genre_group = self.request.GET.get('genre_group', None)
        new_book = self.request.GET.get('new_book', False)
        bestseller = self.request.GET.get('bestseller', False)
        min_price = self.request.GET.get('min_price', 0)
        max_price = self.request.GET.get('min_price', Book.objects.all().aggregate(Max('price')))
        if genre_group:
            book_list = Book.objects.filter(genre__in=Genre.objects.filter(genre_group__in=GenreGroups.objects.filter(name__exact=genre_group)))
        else:
            book_list = Book.objects.all()
        return book_list

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
    

        genre_group = self.request.GET.get('genre_group', 'Любой')
        new_book = self.request.GET.get('new_book', False)
        bestseller = self.request.GET.get('bestseller', False)
        min_price = self.request.GET.get('min_price', 0)
        max_price = self.request.GET.get('max_price', 0)
        if genre_group:
            books = Book.objects.filter(genre__in=Genre.objects.filter(genre_group__in=GenreGroups.objects.filter(name__exact=genre_group)))
        else:
            books = Book.objects.all()
        # context['book_list'] = book_list
        context['genre_group'] = genre_group
        context['new_book'] = new_book
        context['bestseller'] = bestseller
        context['min_price'] = min_price
        context['max_price'] = max_price
        return context
"""
select * from store_book where id in (select book_id from store_book_genre where genre_id in (select genre_id from store_genredepends where genre_group_id in 
(select id from store_genregroups where name='Компьютерная литература')));
"""





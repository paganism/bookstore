from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

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
    model = GenreGroups, Book
    template_name = 'store/catalog.html'
    # context_object_name = 'book_list'
    paginate_by = 8

    def get_queryset(self):
        book_list = Book.objects.all()
        return book_list

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
        
        # book_list = Book.objects.all()
        # context['book_list'] = book_list
        # paginator = Paginator(book_list, 10)
        # context['paginator'] = paginator
        #print(context)
        print(self.request.GET['genre'])
        # print(self.request.GET['new_book'])
        # print(self.request.GET['bestseller'])
        # print(self.request.GET['min_price'])
        # print(self.request.GET['max_price'])

        genre = self.request.GET['genre']
        # new_book = self.request.GET['new_book']
        # best_seller = self.request.GET['bestseller']
        # min_price = self.request.GET['min_price']
        # max_price = self.request.GET['max_price']
        # if max_price < min_price:
        #     max_price = min_price
        books = Book.objects.filter(genre__iexact=genre)
        context['books'] = books
        print(books)
        return context
"""
select * from store_book where id in (select book_id from store_book_genre where genre_id in (select genre_id from store_genredepends where genre_group_id in 
(select id from store_genregroups where name='Компьютерная литература')));
"""
    


class GenrePage(generic.ListView):
    # model = GenreGroups, Book
    # template_name = 'store/catalog.html'
    paginate_by = 7
    def get(self, request):
        #tag = get_object_or_404(Post, slug__iexact=slug)
        genre = self.request.GET['genre']
        new_book = self.request.GET['new_book']
        best_seller = self.request.GET['bestseller']
        min_price = self.request.GET['min_price']
        max_price = self.request.GET['max_price']
        if max_price < min_price:
            max_price = 0
        context = {
            'genre': genre,
            'new_book': new_book,
            'best_seller': best_seller,
            'min_price': min_price,
            'max_price': max_price
        }
        books = Book.objects.filter(Q(genre__icontains=genre), 
                                    Q(new_book__icontains=new_book),
                                    Q(best_seller__icontains=best_seller),
                                    Q(min_price__gt=min_price),
                                    Q(max_price__lt=max_price))
        return render(request, 'store/catalog.html', context=context)
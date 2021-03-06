from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Max, Min

from .forms import FilterForm

from .models import Book, Author, GenreGroups, Genre

from cart.forms import CartAddProductForm

from .utils import get_carousel_img_list


BOOK_NUMBER_IN_MAIN_PAGE = 12
GENRE_GROUPS_LIST = GenreGroups.objects.filter(id__gt=1)


class BookListView(generic.ListView):
    model = Book, GenreGroups
    paginate_by = 10
    template_name = 'store/book_list.html'


    def get_queryset(self):
        book_list = Book.objects.all()[:BOOK_NUMBER_IN_MAIN_PAGE]
        return book_list

    def get_context_data(self, **kwargs):
        carousel_img_list = get_carousel_img_list()
        context = super(BookListView, self).get_context_data(**kwargs)
        context['genregroups_list'] = GENRE_GROUPS_LIST
        context['carousel_img_list'] = carousel_img_list
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        cart_product_form = CartAddProductForm()
        context = super(BookDetailView, self).get_context_data(**kwargs)
        # context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
        context['genregroups_list'] = GENRE_GROUPS_LIST
        context['cart_product_form'] = cart_product_form
        # print(context)
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(author=context['author'])
        context['genregroups_list'] = GENRE_GROUPS_LIST
        print(context['author'])
        return context


class CatalogView(generic.ListView):
    template_name = 'store/catalog1.html'
    paginate_by = 8

    def get_queryset(self):
        genre_group = self.request.GET.get('genre_group', '')
        new_book = self.request.GET.get('new_book', False)
        bestseller = self.request.GET.get('bestseller', False)
        min_price = self.request.GET.get('min_price', 0)
        max_price = self.request.GET.get('max_price', None)
        author = self.request.GET.get('author', None)


        if genre_group:
            book_list = Book.objects.filter(Q(genre__in=Genre.objects.filter(genre_group__in=GenreGroups.objects.filter(name__exact=genre_group)))
                & Q(new_book__exact=new_book) & Q(bestseller__exact=bestseller))
        else:
            book_list = Book.objects.all()
        if not max_price:
            max_price = Book.objects.all().aggregate(Max('price'))

        book_list = book_list.filter(Q(price__gte=min_price) & Q(price__lte=max_price))
        return book_list

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        # context['genregroups_list'] = GenreGroups.objects.filter(id__gt=1)
        context['genregroups_list'] = GENRE_GROUPS_LIST
        genre_group = self.request.GET.get('genre_group', '')
        context['genre_group'] = genre_group

        return context


def catalog_view(request):
    book_list = Book.objects.all()
    # genregroups_list = GenreGroups.objects.filter(id__gt=1)
    genregroups_list = GENRE_GROUPS_LIST
    filter_form = FilterForm(request.GET or None)
    new_book = False
    bestseller = False
    min_price = 0
    max_price = Book.objects.all().aggregate(Max('price'))
    genre_group = ''
    author = ''
    if filter_form.is_valid():
        filters = filter_form.cleaned_data
        if filters['genre_group']:
            genre_group = filters['genre_group']
            book_list = Book.objects.filter(genre__in=Genre.objects.filter(genre_group__in=GenreGroups.objects.filter(name=genre_group)))
        if filters['new_book']:
            book_list = book_list.filter(new_book=filters['new_book'])
            new_book = filters['new_book']
        if filters['bestseller']:
            book_list = book_list.filter(bestseller=filters['bestseller'])
            bestseller = filters['bestseller']
        if filters['min_price']:
            book_list = book_list.filter(price__gte=filters['min_price'])
            min_price = filters['min_price']
        if filters['max_price']:
            book_list = book_list.filter(price__lte=filters['max_price'])
            max_price = filters['max_price']
        if filters['author']:
            book_list = book_list.filter(author__last_name__icontains=filters['author'])
            author = filters['author']
    paginator = Paginator(book_list, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
            'filter_form': filter_form,
            'genregroups_list': genregroups_list,
            'page_obj': page,
            'is_paginated': is_paginated,
            'prev_url': prev_url,
            'next_url': next_url,
            'genre_group': genre_group,
            'min_price': min_price,
            'max_price': max_price,
            'new_book': new_book,
            'bestseller': bestseller,
            'author': author
            }
    return render(request, 'store/catalog.html', context)

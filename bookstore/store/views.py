from django.shortcuts import render
from django.views import generic

from .models import Book, Author, GenreGroups


# Create your views here.
class BookListView(generic.ListView):
    model = Book, GenreGroups
    paginate_by = 3
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


class AuthorDetailView(generic.DetailView):
    model = Author

from django.contrib import admin

from .models import Author, Genre, Book, Language, GenreGroups, GenreDepends


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    list_filter = ('author', 'language', 'genre')


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


@admin.register(GenreGroups)
class GenreGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_group',)
    fields = ['name', 'parent_group']
    list_filter = ('name', 'parent_group',)


@admin.register(GenreDepends)
class GenreDependsAdmin(admin.ModelAdmin):
    list_display = ('genre_group', 'genre',)
    fields = ['genre_group', 'genre']
    list_filter = ('genre_group', 'genre',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ['name',]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['name',]
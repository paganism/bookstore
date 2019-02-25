from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time))


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', related_name='books', help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    COVER_CHOICE = (
        ('s', 'Soft'),
        ('h', 'hard')
    )
    cover = models.CharField(max_length=1, choices=COVER_CHOICE, default='s', help_text='Choose book cover')
    publisher = models.ForeignKey('Publisher', related_name='books', on_delete=models.SET_NULL, null=True)
    sku_code = models.CharField(max_length=20, help_text='Sku code may be only 20 characters')
    pub_year = models.CharField(max_length=4, null=True, blank=True)
    num_pages = models.CharField(max_length=5, null=True, blank=True)
    num_copies = models.CharField(max_length=6, null=True, blank=True)
    AGE_CHOICE = (
        ('0', '0+'),
        ('6', '6+'),
        ('12', '12+'),
        ('16', '16+'),
        ('18', '18+')
    )
    allowed_age = models.CharField(max_length=2, choices=AGE_CHOICE, default='0', help_text='Choose age limit')
    price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    new_book = models.BooleanField(default=False)
    bestseller = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    book_image = models.ImageField(upload_to='img/', width_field=None, null=True)
    
    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created']


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    author_image = models.ImageField(upload_to='img/authors', width_field=None, null=True, default='img/authors/noname.png')
    about = models.TextField(max_length=1000, help_text='Enter a brief author description', null=True, blank=True, default='Here is a brief author description')
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name']


class Language(models.Model):
    name = models.CharField(max_length=30, help_text='Enter a book language')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre')

    def __str__(self):
        return self.name


class GenreGroups(models.Model):
    name = models.CharField(max_length=150, unique=True, help_text='Enter genre group name')
    parent_group = models.ForeignKey('GenreGroups', default=-1, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True)
    genre = models.ManyToManyField('Genre', related_name='genre_group')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, help_text='Enter publisher group name')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    COVER_CHOICE = (
        ('s', 'Soft'),
        ('h', 'hard'),
    )
    cover = models.CharField(max_length=1, choice=COVER_CHOICE, default='s', help_text='Choose book cover')
    publisher = models.CharField(max_length=100)
    sku_code = models.CharField(max_length=20, help_text='Sku code may be only 20 characters', index=True)
    pub_year = models.CharField(max_length=4, null=True, blank=True)
    num_pages = models.CharField(max_length=5)
    num_copies = models.CharField(max_length=6)
    AGE_CHOICE = (
        ('0', '0+'),
        ('6', '6+'),
        ('12', '12+'),
        ('16', '16+'),
        ('18', '18+'),
    )
    allowed_age = models.CharField(max_length=2, choice=AGE_CHOICE, default='0', help_text='Choose age limit')
    price = models.CharField(max_length=6)
    
    
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('books', args=[str(self.id)])


    class Author(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField(null=True, blank=True)
        date_of_death = models.DateField(null=True, blank=True)

        def __str__(self):
            return '{} {}'.format(self.last_name, self.first_name)
            

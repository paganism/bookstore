from django import forms
from django.core.exceptions import ValidationError
from .models import GenreGroups, Genre, Book, Author
from django.db.models import Max


class FilterForm(forms.Form):
    genre_group = forms.ModelChoiceField(required=False, label='Выберите жанр', queryset=GenreGroups.objects.filter(id__gt=1), to_field_name='name', empty_label='')
    new_book = forms.BooleanField(label='Новинки', required=False)
    bestseller = forms.BooleanField(label='Бестселлер', required=False)
    min_price = forms.DecimalField(label='Цена от', max_digits=10, min_value=0, max_value=9999, required=False)
    max_price = forms.DecimalField(label='Цена до', max_digits=10, min_value=0, max_value=10001, required=False)
    author = forms.CharField(label='Автор', max_length=50, required=False)


    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        max_price = cleaned_data.get('max_price')
        min_price = cleaned_data.get('min_price')
        if not cleaned_data.get('min_price'):
            min_price = 0
        
        if not cleaned_data.get('max_price'):
            max_price = Book.objects.all().aggregate(Max('price')).get('price__max')
        print(min_price)
        print(max_price)
        if int(min_price) > int(max_price):
            self.add_error('min_price', 'Максимальная цена должна быть больше минимальной')
        cleaned_data['max_price'] = max_price
        cleaned_data['min_price'] = min_price
        print(cleaned_data)
        return cleaned_data
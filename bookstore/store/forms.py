from django import forms

from .models import GenreGroups, Genre, Book, Author


class FilterForm(forms.Form):
    genre_group = forms.ModelChoiceField(required=False, label='Выберите жанр', queryset=GenreGroups.objects.filter(id__gt=1), to_field_name='name', empty_label='')
    new_book = forms.BooleanField(label='Новинки', required=False)
    bestseller = forms.BooleanField(label='Бестселлер', required=False)
    min_price = forms.DecimalField(label='Цена от', max_digits=10, min_value=0, max_value=9999, required=False)
    max_price = forms.DecimalField(label='Цена до', max_digits=10, min_value=0, max_value=10000, required=False)


    def check_min_max_price(self):
        print('HERERERERERE1')
        try:
            print('HERERERERERE0')
            min_price = self.cleaned_data.get['min_price']
            max_price = self.cleaned_data.get['max_price']
        except:
            print('HERERERERERE1')
            min_price = 0
            max_price = Book.objects.all().aggregate(Max('price'))
        if min_price > max_price:
            raise forms.ValidationError('Enter valid price range')
        print('HERERERERERE2')
        return min_price

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter book price'}),
            'edition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book edition'}),
        }

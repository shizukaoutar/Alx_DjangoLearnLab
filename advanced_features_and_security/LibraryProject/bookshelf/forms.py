from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    publication_year = forms.IntegerField()
    




class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  


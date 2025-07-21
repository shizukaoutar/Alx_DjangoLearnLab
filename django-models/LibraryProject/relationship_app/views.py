from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)




class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


def login_view(request):
    return auth_views.LoginView.as_view(template_name='relationship_app/login.html')
    '''if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'list_books')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})'''
    
def logout_view(request):
    return auth_views.LogoutView.as_view(template_name='relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)    
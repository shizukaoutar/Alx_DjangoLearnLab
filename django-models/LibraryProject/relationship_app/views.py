from django.contrib.auth.decorators import permission_required, user_passes_test
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile
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


def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    
    context = {'form': form}
    return render(request, 'relationship_app/add_book.html', context)


@permission_required('relationship_app.can_edit_book', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    
    context = {'form': form}
    return render(request, 'relationship_app/edit_book.html', context)

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
   if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('list_books')
   else:
       book = Book.objects.get(pk=pk)
       context = {'book': book}
       return render(request, 'relationship_app/delete_book.html', context)

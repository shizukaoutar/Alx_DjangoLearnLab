from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    
    context = {'form': form}
    return render(request, 'bookshelf/add_book.html', context)

@permission_required('bookshelf.can_view_book', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookshelf/list_books.html', context)

@permission_required('bookshelf.can_edit_book', raise_exception=True)
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
    return render(request, 'bookshelf/edit_book.html', context)

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, pk):
   if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('list_books')
   else:
       book = Book.objects.get(pk=pk)
       context = {'book': book}
       return render(request, 'bookshelf/delete_book.html', context)

""" # Creating permissions
can_view = Permission.objects.get(codename='can_view_book')
can_create = Permission.objects.get(codename='can_create_book')
can_edit = Permission.objects.get(codename='can_edit_book')
can_delete = Permission.objects.get(codename='can_delete_book')


# Creating groups
Editors = Group.objects.create(name='Editors')
Viewers = Group.objects.create(name='Viewers')
Admins = Group.objects.create(name='Admins')

# Assigning permissions to groups
Editors.permissions.add(can_create, can_edit, can_delete)
Viewers.permissions.add(can_view)
Admins.permissions.add(can_view, can_create, can_edit, can_delete) """


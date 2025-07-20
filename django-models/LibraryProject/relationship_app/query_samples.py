books_by_author = Book.objects.filter(author__name='John Doe')
print(books_by_author)

books = Library.objects.get(name='Library 1')
print(books.all())


librarian = Librarian.objects.get(library__name='Library 1')
print(librarian)
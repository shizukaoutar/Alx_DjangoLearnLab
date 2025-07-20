books_by_author = Book.objects.filter(author__name='John Doe')
print(books_by_author)

books = Book.objects.filter(libraries__name='Library 1')
print(books.all())


librarian = Librarian.objects.filter(library__name='Library 1')
print(librarian)
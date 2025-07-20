books_by_author = Book.objects.filter(author__name='John Doe')
print(books_by_author)

books = Book.objects.get(libraries__name='Library 1')
print(books)


librarian = Librarian.objects.get(library__name='Library 1')
print(librarian)
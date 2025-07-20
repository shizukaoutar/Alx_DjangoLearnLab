books_by_author = Book.objects.filter(author__name='John Doe')
print(books_by_author)

books = Book.objects.all()
print(books)


librarian = Librarian.objects.filter(library__name='Library 1')
print(librarian)
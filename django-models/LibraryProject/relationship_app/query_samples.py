books_by_author = Book.objects.filter(author__name=author_name)
print(books_by_author)

books = Library.objects.get(name=library_name)
print(books.all())


librarian = Librarian.objects.get(library__name=library_name)
print(librarian)
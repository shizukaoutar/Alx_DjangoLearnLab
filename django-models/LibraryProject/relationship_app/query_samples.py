###Query all books by a specific author.
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(books)

###Query all books in a specific library.
books = Library.objects.get(name=library_name)
print(books.all())

###Query the librarian of a specific library.
librarian = Librarian.objects.get(library__name=library_name)
print(librarian)
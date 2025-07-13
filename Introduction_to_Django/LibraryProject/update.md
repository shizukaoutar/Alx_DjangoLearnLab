commands:
new_book.title = 'Nineteen Eighty-Four'
new_book.save()
books = Book.objects.all()
for book in books:
    print (f"{book.title} by {book.author} in {book.publication_year}")
output:
Nineteen Eighty-Four by George Orwell in 1949

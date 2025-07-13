commands:
book = Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')
output:
nothing, meaning the code is successful

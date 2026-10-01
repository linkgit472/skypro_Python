from book import Book

library = [
    Book('Преступление и наказание', 'Достоевский М.Ф.'),
    Book('Война и мир', 'Толстой Л.Н.'),
    Book('Мертвые души', 'Гоголь Н.В.')
]

for book in library:
    print(book.bookTitle, '-', book.bookAuthor)

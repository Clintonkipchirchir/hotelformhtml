#filter books by specific author
from relationship_app.models import Book, Author, Library, Librarian

name = book.author.name
list_books_by_author = Book.objects.filter(author__name=name)

#get all books in a library
all_books_in_library = library.books.all()

#retrieve librarian for a library
my_library = library.name
my_librarian = librarian.objects.get(library__name=my_library)
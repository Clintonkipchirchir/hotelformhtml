#filter books by specific author
from relationship_app.models import Book, Author, Library, Librarian

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

#get all books in a library
all_books_in_library = Library.objects.get(name=library_name)
books_in_library = all_books_in_library.books.all()

#retrieve librarian for a library
my_library = library.name
my_librarian = librarian.objects.get(library__name=my_library)
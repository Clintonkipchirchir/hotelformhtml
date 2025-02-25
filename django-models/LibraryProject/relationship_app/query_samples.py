#filter books by specific author
from relationship_app.models import Book, Author, Library, Librarian

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

#get all books in a library
library_name = Library.objects.get(name=library_name)
books_in_library = library_name.books.all()

#retrieve librarian for a library
my_librarian = Librarian.objects.get(library=
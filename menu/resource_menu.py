from library.author import Author
from library.resources import Book
from library.utils import get_available_copies, get_borrowed_count, search_books, filter_books
from library import file_io


def add_book(books):
    title = input("Title: ")
    author_name = input("Author name: ")
    nationality = input("Nationality (optional): ") or None
    birth_year = input("Birth year (optional): ") or None

    author = Author(author_name, nationality, birth_year)

    isbn = input("ISBN: ")
    year = input("Publication year: ")
    category = input("Category (optional): ") or "General"
    copies = int(input("Number of copies: "))

    book = Book(title, author, isbn, year, category, copies)
    books.append(book)
    file_io.save_books(books)
    print("Book added successfully.")


def list_books(books, borrows):
    print("\nBooks in library:")
    for b in books:
        available = get_available_copies(b, borrows)
        borrowed = get_borrowed_count(b, borrows)
        print(f"{b} | Available: {available} | Borrowed: {borrowed}")


def search_book_cli(books):
    field = input("Search by (title/author/isbn/category/year): ").lower()
    query = input("Enter search query: ")

    results = search_books(books, query, field)

    if results:
        for b in results:
            print(b)
    else:
        print("No books found.")


def filter_books_cli(books, borrows):
    criteria = input("Filter by (available/borrowed/category): ").lower()
    category = None

    if criteria == "category":
        category = input("Enter category: ")

    results = filter_books(books, borrows, criteria, category)

    if results:
        for b in results:
            available = get_available_copies(b, borrows)
            borrowed = get_borrowed_count(b, borrows)
            print(f"{b} | Available: {available} | Borrowed: {borrowed}")
    else:
        print("No books match the filter criteria.")


def delete_book(books, borrows):
    isbn = input("Enter ISBN of the book to delete: ")
    book = next((b for b in books if b.isbn == isbn), None)

    if not book:
        print("Book not found.")
        return

    active_borrows = [b for b in borrows if b.book_title == book.title and not b.return_date]

    if active_borrows:
        print("Cannot delete. Some copies are currently borrowed.")
        return

    books.remove(book)
    file_io.save_books(books)
    print(f"Book {book.title} deleted successfully.")


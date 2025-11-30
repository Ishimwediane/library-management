from library.resources import Book
from library.author import Author
from library.borrow import Borrow
from library import file_io
from library.utils import search_books, filter_books, get_available_copies, get_borrowed_count


#FUNCTIONS

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


def borrow_book(books, borrows):
    isbn = input("ISBN of book to borrow: ")
    book_to_borrow = next((b for b in books if b.isbn == isbn), None)

    if not book_to_borrow:
        print("Book not found.")
        return

    available = get_available_copies(book_to_borrow, borrows)
    if available <= 0:
        print("No available copies to borrow.")
        return

    borrower = input("Your name: ")
    borrow_record = Borrow(borrower, book_to_borrow.title)

    borrows.append(borrow_record)
    file_io.save_borrows(borrows)
    print(f"Book borrowed successfully! Due date: {borrow_record.due_date}")


def return_book(books, borrows):
    borrower = input("Your name: ")
    isbn = input("ISBN of book to return: ")

    book_to_return = next((b for b in books if b.isbn == isbn), None)

    if not book_to_return:
        print("Book not found.")
        return

    borrow_record = next(
        (b for b in borrows if b.borrower_name == borrower and
         b.book_title == book_to_return.title and b.return_date is None),
        None
    )

    if borrow_record:
        borrow_record.mark_returned()
        file_io.save_borrows(borrows)
        print("Book returned successfully.")
    else:
        print("No active borrow record found for this book and borrower.")


def list_borrows(borrows):
    print("\nBorrow records:")
    for b in borrows:
        status = "Returned" if b.return_date else ("Overdue" if b.is_overdue() else "Borrowed")
        print(f"{b} | Status: {status}")


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


# menu-cli#

def cli():
    books = file_io.load_books()
    borrows = file_io.load_borrows()

    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. List all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. List borrow records")
        print("6. Search a book")
        print("7. Filter records")
        print("8. Delete a book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            list_books(books, borrows)

        elif choice == "3":
            borrow_book(books, borrows)

        elif choice == "4":
            return_book(books, borrows)

        elif choice == "5":
            list_borrows(borrows)

        elif choice == "6":
            search_book_cli(books)

        elif choice == "7":
            filter_books_cli(books, borrows)

        elif choice == "8":
            delete_book(books, borrows)

        elif choice == "9":
            file_io.save_books(books)
            file_io.save_borrows(borrows)
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

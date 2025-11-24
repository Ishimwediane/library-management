from library.author import Author
from library.resources import Book
from library.borrow import Borrow
from library import file_io


def main():
    # Load existing data
    books = file_io.load_books()
    borrows = file_io.load_borrows()

    print("Welcome to the Library Inventory System!\n")

    while True:
        print("Menu:")
        print("1. Add a book")
        print("2. List all books")
        print("3. Borrow a book")
        print("4. List borrow records")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new book
            title = input("Book title: ")
            author_name = input("Author name: ")
            nationality = input("Author nationality (optional): ")
            birth_year = input("Author birth year (optional): ")
            isbn = input("ISBN: ")
            category = input("Category (optional): ")
            year = input("Publication year (optional): ")

            # Convert year and birth_year to int if provided
            birth_year = int(birth_year) if birth_year else None
            year = int(year) if year else None

            author = Author(author_name, nationality, birth_year)
            book = Book(title, author, isbn, category, year)

            books.append(book)
            file_io.save_books(books)
            print(f"Book '{title}' added!\n")

        elif choice == "2":
            # List all books
            if not books:
                print("No books in the library.\n")
            else:
                print("Books in library:")
                for b in books:
                    print(b)
                print()

        elif choice == "3":
            # Borrow a book
            borrower = input("Borrower name: ")
            isbn = input("ISBN of book to borrow: ")

            # Find the book
            book_to_borrow = next((b for b in books if b.isbn == isbn), None)
            if not book_to_borrow:
                print("Book not found.\n")
            else:
                borrow_record = Borrow(borrower, book_to_borrow.title)
                borrows.append(borrow_record)
                file_io.save_borrows(borrows)
                print(f"{borrower} borrowed '{book_to_borrow.title}'.\n")

        elif choice == "4":
            # List borrow records
            if not borrows:
                print("No borrow records.\n")
            else:
                print("Borrow Records:")
                for r in borrows:
                    print(r)
                print()

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

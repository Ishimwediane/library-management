from library import file_io
from menu.borrow_menu import borrow_book, return_book, list_borrows
from menu.resource_menu import add_book, list_books, search_book_cli, filter_books_cli, delete_book


def cli():
    books = file_io.load_books()
    borrows = file_io.load_borrows()

    actions = {
        "1": lambda: add_book(books),
        "2": lambda: list_books(books, borrows),
        "3": lambda: borrow_book(books, borrows),
        "4": lambda: return_book(books, borrows),
        "5": lambda: list_borrows(borrows),
        "6": lambda: search_book_cli(books),
        "7": lambda: filter_books_cli(books, borrows),
        "8": lambda: delete_book(books, borrows),
        "9": lambda: (
            file_io.save_books(books),
            file_io.save_borrows(borrows),
            print("Exiting...")
        )
    }

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

        action = actions.get(choice, lambda: print("Invalid choice. Try again."))
        action()

        if choice == "9":
            break

from library.resources import Book
from library.author import Author
from library.borrow import Borrow
from library import file_io
from datetime import date
from library.utils import search_books,filter_books,get_available_copies



def get_available_copies(book, borrows):
    borrowed_count = sum(1 for b in borrows if b.book_title == book.title and b.return_date is None)
    return book.copies - borrowed_count

def main():
    books = file_io.load_books()
    borrows = file_io.load_borrows()
    
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. List all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. List borrow records")
        print("6. search a book")
        print("7. filter records")
        print("8. Delete a book")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
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

        elif choice == "2":
            print("Books in library:")
            for b in books:
                available = get_available_copies(b, borrows)
                print(f"{b} | Available copies: {available}")

        elif choice == "3":
            isbn = input("ISBN of book to borrow: ")
            book_to_borrow = next((b for b in books if b.isbn == isbn), None)
            if not book_to_borrow:
                print("Book not found.")
            elif get_available_copies(book_to_borrow, borrows) <= 0:
                print("No available copies to borrow.")
            else:
                borrower = input("Your name: ")
                borrow_record = Borrow(borrower, book_to_borrow.title)
                borrows.append(borrow_record)
                file_io.save_borrows(borrows)
                print(f"Book borrowed successfully! Due date: {borrow_record.due_date}")

        elif choice == "4":
            borrower = input("Your name: ")
            isbn = input("ISBN of book to return: ")
            book_to_return = next((b for b in books if b.isbn == isbn), None)
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

        elif choice == "5":
            print("Borrow records:")
            for b in borrows:
                status = "Returned" if b.return_date else ("Overdue" if b.is_overdue() else "Borrowed")
                print(f"{b} | Status: {status}")
                
        elif choice == "6":
            field = input("Search by (title/author/isbn/category/year): ").lower()
            query = input("Enter search query: ")
            results = search_books(books, query, field)
            for b in results:
             print(b)

        elif choice == "7":
            criteria = input("Filter by (available/borrowed/category): ").lower()
            category = None
            if criteria == "category":
                category = input("Enter category: ")
            results = filter_books(books, borrows, criteria, category)
            if results:
                print("Filter results:")
                for b in results:
                    available = get_available_copies(b, borrows)
                    print(f"{b} | Available copies: {available}")
            else:
                print("No books match the filter criteria.")
        
        elif choice == "8":
              isbn = input("Enter ISBN of the book to delete: ")
              book = next((b for b in books if b.isbn == isbn), None)
              if not book:
                print("Book not found.")
                continue
              active_borrows = [b for b in borrows if b.book_title == book.title and not b.return_date]
              if active_borrows:
                 print("Cannot delete. Some copies are currently borrowed.")
                 continue
              books.remove(book)
              file_io.save_books(books)
              print(f"Book {book.title} deleted successfully.")
      
                
        elif choice == "9":
            file_io.save_books(books)
            file_io.save_borrows(borrows)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

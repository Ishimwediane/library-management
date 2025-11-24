def search_books(books, query, field):
    query = query.lower()
    results = []
    for book in books:
        if field == "title" and query in book.title.lower():
            results.append(book)
        elif field == "author" and query in book.author.name.lower():
            results.append(book)
        elif field == "isbn" and query in book.isbn.lower():
            results.append(book)
        elif field == "category" and book.category and query in book.category.lower():
            results.append(book)
        elif field == "year" and book.year and query in str(book.year):
            results.append(book)
    return results

def filter_books(books, borrows, criteria, category=None):
    filtered = []
    for book in books:
        available = get_available_copies(book, borrows)
        if criteria == "available" and available > 0:
            filtered.append(book)
        elif criteria == "borrowed" and available == 0:
            filtered.append(book)
        elif criteria == "category" and category and book.category.lower() == category.lower():
            filtered.append(book)
    return filtered

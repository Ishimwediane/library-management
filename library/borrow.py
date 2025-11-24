from .resources import LibraryResource

class Borrow(LibraryResource):
    """class for Author"""
    def __init__(self,borrower_name,book_title,borrow_date=None,return_date=None):
        
        super().__init__(borrower_name)
        self.borrower_name = borrower_name
        self.book_title = book_title
        self.borrow_date = borrow_date
        self.return_date = return_date
            
    def __repr__(self):
        return (f"Borrow(borrower_name={self.borrower_name}, book_title={self.book_title}, borrow_date={self.borrow_date}, return_date={self.return_date})")
    
    def __eq__(self, other):
        if not isinstance(other, Borrow):
            return False
        return (self.borrower_name == other.borrower_name and self.book_title == other.book_title and self.borrow_date == other.borrow_date and self.return_date == other.return_date)
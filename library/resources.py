from abc import ABC, abstractmethod

class LibraryResource(ABC):
    """abstract class for library resources"""
    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def __eq__(self, other):
        pass
   
class Book(LibraryResource):
    """class for books"""
    def __init__(self, title, author,isbn,year,category :str="General"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.category = category
        self.available=False
        
    def __repr__(self):
        return (f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, year={self.year}, category={self.category}, available={self.available})")
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        
        return self.isbn == other.isbn
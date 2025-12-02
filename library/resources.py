from abc import ABC, abstractmethod

class LibraryResource(ABC):
    def __init__(self,title):
        self.title = title
    
    """abstract class for library resources"""
    
    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def __eq__(self, other):
        pass
   
class Book(LibraryResource):
    """class for books"""
    def __init__(self, title, author,isbn,year,category :str="General",copies=1):
        
        self._title=None
        
        self._isbn=None
        self._category=None
        
        
        self.title = title
        self._author = author
        self.isbn = isbn
        self.year = year
        self.category = category
        self.copies = copies
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if not value.replace(" ","").isalpha():
            raise ValueError("title must contain only space and letters")
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value
    
    
    
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self,value):
        if not value:
            raise ValueError("ISBN cannot be empty")
        self._isbn = value
    

    
    def __repr__(self):
        return (f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, year={self.year}, category={self.category}")
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        
        return self.isbn == other.isbn
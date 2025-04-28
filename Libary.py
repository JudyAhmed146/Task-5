class books:
    def _init_( self,title,author,ISBN,available):
        self.title=title
        self.author=author  
        self.ISBN=ISBN
        self.available=available

class Members :
    def _init_( self, name , ID , borrowed_book, return_book):
        self.name=name
        self.ID=ID    
        self.borrowed_books=borrowed_book
        self.return_book=return_book
        borrowed_book(self)=books.title
        
    def borrowed_books(self):
        if self.available == True :
            return "available for borrowing"
        else: self.available==False
        return"not available for borrowing"
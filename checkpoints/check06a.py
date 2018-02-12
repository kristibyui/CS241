"""
CS241 Checkpoint 6A
Written by Chad Macbeth
"""

### Represents any book
class Book:

    ### Initialize a book object
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    ### Get book data from user
    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    ### Display book data
    def display_book_info(self):
        print("{} ({}) by {}" .format(self.title, self.publication_year, self.author))

### Represents a Textbook which is derived from a Book
class TextBook(Book):

    ### Initialize a TextBook object
    def __init__(self):
        super().__init__()
        self.subject = ""

    ### Get Textbook specific information from the user
    def prompt_subject(self):
        self.subject = input("Subject: ")
   
    ### Display Textbook specific information 
    def display_subject(self):
        print("Subject: {}" .format(self.subject))

### Represents a PictureBook which is derived from a Book
class PictureBook(Book):

    ### Initialize a PictureBook object
    def __init__(self):
        super().__init__()
        self.illustrator = ""

    ### Get Picturebook specific information from the user
    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")
 
    ### Display Picturebook specific information 
    def display_illustrator(self):
         print("Illustrated by {}" .format(self.illustrator))

### Test the classes created above
def main():
    book = Book()
    book.prompt_book_info()
    print()
    book.display_book_info()
    print()

    text = TextBook()
    text.prompt_book_info()
    text.prompt_subject()
    print() 
    text.display_book_info()
    text.display_subject()
    print()

    picture = PictureBook()
    picture.prompt_book_info()
    picture.prompt_illustrator()
    print()
    picture.display_book_info()
    picture.display_illustrator()


if __name__ == "__main__":
    main()

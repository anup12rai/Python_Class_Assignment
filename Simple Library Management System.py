# Create a base class LibraryItem with attributes title and year.
# Then, create two derived classes Book and Magazine that include
# additional attributes specific to books and magazines, respectively.
# Implement a method display_info() in both derived classes to display detailed information about the items. 
# Demonstrate polymorphism by creating a list of library items and displaying their information.

class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year

class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author
        

    def display_info(self):
        print(f"Book: {self.title}\nYear: {self.year}\nAuthor: {self.author}")


class Magazine(LibraryItem):
    def __init__(self, title, year,editor):
        super().__init__(title, year)
        
        self.editor = editor

    def display_info(self):
        print(f"Magazine: {self.title}\nYear: {self.year}\nEditor: {self.editor}")


library_items = [
    Book("somthing is nothing", 2024, "Aniruddha"),
    Magazine("python", 2024,"sudip")
    
]

for item in library_items:
    item.display_info()

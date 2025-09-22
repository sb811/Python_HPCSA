'''

Assignment 1: Define a class named Book that represents a book in a library.
    • Attributes :
    • title (string): The title of the book.
    • author (string): The author of the book.
    • year (integer): The year the book was published.
    • available (boolean): A status indicating whether the book is available or
      checked out.

    • Methods:
    • display_details() that prints the book’s details (title, author, and year).
      Constructor to set values of books

    • Tasks:
    • Create at least two objects of the Book class with different attributes,
      initialize values using constructor
    • Display the details of each book using the display_details method.

'''

# class Book:
#     def __init__(self,title,author,year,available):
#         self.title=title
#         self.author=author
#         self.year=year
#         self.available=available
    
#     def display_info(self):
#         print(f'''
# Year                    Author                  Title                              Availability
# -------------------------------------------------------------------------------------------------------------
# {self.year}             {self.author}           {self.title}                                      {self.available}''')



# b1=Book("Harry Potter","J K Rowllings",2003,True)
# b2=Book("Too Good to be true","Prajakta Koli",2025,False)


# b1.display_info()
# b2.display_info()



'''

Assignment 2:

    • Create a class shape
    • Create sub classes Circle and Rectangle inherited from shape
    • Write a function print_shape_area(shape) that takes an instance of Shape (or any
      subclass of Shape) and prints the area of the shape.
    • Create instances of Circle and Rectangle.
    • Call the print_shape_area function with these instances to demonstrate
      polymorphism.


'''

class Shape:
    def print_shape_area(self):
        print("This is Shape class")

    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.PI = 3.14

    def print_shape_area(self):
        area = self.PI * self.radius ** 2
        print(f'The Area of the Circle is {area:.2f} cm²')


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_shape_area(self):
        area = self.length * self.breadth
        print(f'The Area of the Rectangle is {area} cm²')


def print_area(shape_instance):
    shape_instance.print_shape_area()


circle_obj = Circle(5)
rectangle_obj = Rectangle(5, 2)
shape_obj = Shape()

print_area(shape_obj)
print_area(circle_obj)
print_area(rectangle_obj)


        




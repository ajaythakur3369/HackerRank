'''
Task:-
Given a Book class and a Solution class, write a MyBook class that does the following:
 Inherits from Book
 Has a parameterized constructor taking these 3 parameters:
 1. string title
 2. string author
 3. int price
 Implements the Book class' abstract display() method so it prints these 3 lines:
 1. Title:, a space, and then the current instance's title.
 2. Author:, a space, and then the current instance's author.
 3. Price:, a space, and then the current instance's price.
'''

'''
Input Format:- 
You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments). It then calls the display method on the Book object.
'''

'''
Output Format:- 
The void display() method should print and label the respective title, author, and price of the MyBook object's instance (with each value on its own line) like so:

Title: $title
Author: $author
Price: $price
'''

'''
Sample Input:- 
The following input from stdin is handled by the locked stub code in your editor:

The Alchemist
Paulo Coelho
248
'''

'''
Sample Output:-
The following output is printed by your display() method:

Title: The Alchemist
Author: Paulo Coelho
Price: 248
'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

'''
Write MyBook class
'''

class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: " + self.title + "\nAuthor: " + self.author + "\nPrice: " + str(self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

'''
Input (stdin):-
The Alchemist
Paulo Coelho
248
'''

'''
Expected Output:- 
Title: The Alchemist
Author: Paulo Coelho
Price: 248
'''



















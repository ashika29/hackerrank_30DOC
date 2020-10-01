# Question link: https://www.hackerrank.com/challenges/30-abstract-classes/problem
# Code section:


#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        return super(MyBook, self).__init__(title, author)
    def display(self):
        print("Title: %s"%(self.title))
        print("Author: %s"%(self.author))
        print("Price: %d"%(self.price))


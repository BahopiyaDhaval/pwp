#Bahopiya Dhaval
class Book:
    def __init__(self, title, author, price):
        self.title, self.author, self.price = title, author, price
    def display(self):
        print(self.title, "-", self.author, "- Rs.", round(self.price, 2))
    def discount(self, percent):
        self.price -= self.price * percent / 100

# (a)
b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 500)
b2 = Book("1984", "George Orwell", 400)
b1.display(); b2.display()

# (b)
b1.discount(10)
b1.display()

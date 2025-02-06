#Task 1
class StringHandler:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input(" ")

    def printString(self):
        print(self.text.upper())

#Task 2
    def __init__(self):
        self.area = 0

    def show_area(self):
        print(f"Area: {self.area}")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def calculate_area(self):
        self.area = self.length * self.length
        print(f"Area of square: {self.area}")

#Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width
        print(f"Area of rectangle: {self.area}")

#Task 4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        print(f"Distance: {distance}")

#Task 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

#Task 6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

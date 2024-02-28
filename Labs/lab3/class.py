
#*1 task 
class Input_output():
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())

strater = Input_output()
strater.getString()
strater.printString()

#*2 task
class Shape():
    def __init__(self):
        pass
    
    def area(self):
        print("default area is 0")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length 
    
    def area(self):
        print(f"Area of square is {self.length * self.length}")
 
#*3 task   
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        print(f"Area of rectangle is {self.width * self.height}")
        

area =Shape()
area.area()

side = int(input())

area_of_square = Square(side)
area_of_square.area()     

width = int(input())
height = int(input())

area_of_rectangle = Rectangle(width, height)
area_of_rectangle.area()


#*4 task
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"(coordinates are: {self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.show()
        
    def dist(self, other_x, other_y):
        print(f"distance between two points is: {((self.x - other_x) ** 2 + (self.y - other_y) ** 2) ** 0.5}")
        

p1 = Point(2, 5)
p1.show()
p1.move(3, 5)
p1.dist(2, 6)


#*5 task
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, login, add_balance):
        if self.owner == login:   
            self.balance += add_balance
        else:
            print('you do not have account')
    
    def withdraw(self, login, withdrawal):
        if self.owner == login: 
            if self.balance < withdrawal:
                print(f"you cannot withdrawal this money, your balance is: {self.balance}")
            else:
                print(f"operation complited, now your balance is: {self.balance}")
                self.balance -= withdrawal
        else:
            print('you do not have account')
            
    def my_balance(self, login):
        if self.owner == login:  
            print(f"Your balance is: {self.balance}")
        else:
            print('you do not have account')

owner = str(input())  
mypay = Account("Kanysh", 100)
mypay.deposit(owner, 1500)
mypay.my_balance(owner)
mypay.withdraw(owner, 1000)
mypay.my_balance(owner)
mypay.withdraw(owner, 700)


#*6 task
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime = list(filter(lambda x: is_prime(x), n))
print(prime)    
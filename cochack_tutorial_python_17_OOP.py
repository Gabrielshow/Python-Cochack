#python contd
def decor(func):
    def wrap():
        print("======")
        func()
        print("======")
    return wrap

def print_text():
    print("hello, world!")
    
decorated = decor(print_text)
decorated()

#if we are defining a function name then we can decorate it with the @ symbol

@decor
def print_text1():
    print("hello world")

print_text1()
#this above is equivalent to print_text2 = decor(print_text2)
#print_text()

# my_func = my_dec(my_func) is eqv to @my_dec

#filtering values
nums = [11, 22, 33, 47, 87]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

#class methods
#they are marked with the classmethod decorator
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.width
    
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
    
square = Rectangle.new_square(5)
print(square.calculate_area())

#self and cls are just conventions

class Person():
    def __init__(self, name):
        self.name = name
        
    @classmethod
    def sayHi(cls):
        print("Hi ")

#static methods are similar to class methods except they don't receive any additional arguments
#they are marked with static method decorator

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        
    @staticmethod
    def validate_toppings(toppings):
        if toppings == "pineapple":
            raise ValueError("No paps")
        else:
            return True
        
toppings = ["cheese" , "onions", "spam"]
if all(Pizza.validate_toppings(i) for i in toppings):
    pizza = Pizza(toppings)
#need to fix code outputs Pizza() takes no argument

# property
# created by putting a property decorator above a method

class Pizza1:
    def __init__(self, toppings):
        self.toppings = toppings
        
    @property
    def pineapple_allowed(self):
        return False
    
Pizza = Pizza1(["cheese", "tomato"])
print(Pizza.pineapple_allowed)
# Pizza.pineapple_allowed = True

# getters and setteres
class Pizza2:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password ")
            if password == 'swordfish':
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert!, Intruder!")
    
pizza = Pizza2(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
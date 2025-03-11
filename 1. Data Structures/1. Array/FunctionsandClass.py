# Functions:
#structure of the function is as follows:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
# Calling the function
num = 5;
print("Factorial of", num, "is", factorial(num))


# Class Definition and Basic Object Creation
# Structure of the class is as follows:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_car_info(self):
        return f"Car Make:{self.make}, Model:{self.model}, Year:{self.year}"
    
# Creating an object of the class
mycar1 = Car("BMW", "XM", 2025)
print(mycar1.display_car_info())
mycar2 = Car("Mini", "Cooper", 2025)
print(mycar2.display_car_info())


# Example 2:

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_book_info(self):
        return f"Book Title:{self.title}, Author:{self.author}, Year:{self.year}"
    
# Creating an object of the class
book1 = Book("Python Programming", "John Doe", 2020)
print(book1.display_book_info())
book2 = Book("Java Programming", "Jane Doe", 2020)
print(book2.display_book_info())

# Class with Methods       
#Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.width + self.length)

#Creating an object of the class
rect1 = Rectangle(5, 10)
print("Area of the rectangle is:", rect1.area())
print("Perimeter of the rectangle is:", rect1.perimeter())


# Class Inheritance
# Structure of the class is as follows:
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Some Sound"
    
# Creating a subclass of Animal class called Dog class which inherits the properties of the Animal class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Creating a subclass of Animal class called Cat class which inherits the properties of the Animal class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating an Instances of the Dog class and Cat class
my_dog = Dog("Buddy")
my_cat = Cat("Kitty")

# Calling the speak method of the Dog class and Cat class
print(my_dog.speak())
print(my_cat.speak())

# Example 2:


class Flyer:
    def fly(self):
        return "I can Flying"

class Swimmer:
    def swim(self):
        return "I can swim"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack Quack"

my_duck = Duck()
print(my_duck.fly())
print(my_duck.swim())
print(my_duck.quack())


# Multiple Inheritance Example 3:
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def drive(self):
        return f"{self.brand} is being driven"
    
# Parent class for electric vehicles
class Electric:
    def charge(self):
        return "Electric car is being charged"

# Child class inheriting from both Vehicle and Electric classes
class ElectricCar(Vehicle, Electric):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def display_info(self):
        return f"{self.brand} {self.model}"

# Creating an object of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model S")
print(my_electric_car.display_info())
print(my_electric_car.drive())
print(my_electric_car.charge())

#Example 4: Simple Banking System
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New Balance:{self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return f"Withdrew {amount}. New Balance:{self.balance}"
    
    def display_balance(self):
        return f"Account Name:{self.account_name}, Balance:{self.balance}"

# Creating an object of the BankAccount class
my_account = BankAccount(123456, "John")
print(my_account.display_balance())
print(my_account.deposit(1000))
print(my_account.withdraw(500))
print(my_account.display_balance())

#Example 6:Currency Conversion Example with Multiple Inheritance
# Parent class for currency conversion

class CurrencyConversion:
    def __init__(self):
        self.rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110.0,
            "CNY": 7.0,
            "INR": 74.0
        }
    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency: %s" % from_currency)
        # Convert the amount to a currency then to target currency
        amount_in_usd = amount / self.rates[from_currency]
        return amount_in_usd * self.rates[to_currency]

# Parent class for formatting currency
class Formatter:
    def format_currency(self, amount, currency):
        return f"{currency} {amount:.2f}"

# Child class inheriting from both CurrencyConversion and Formatter classes
class CurrencyConverter(Formatter, CurrencyConversion):
    def convert_and_format(self, amount, from_currency, to_currency):
        converted_amount = self.convert(amount, from_currency, to_currency)
        return self.format_currency(converted_amount, to_currency)

if __name__ == "__main__":
    converter = CurrencyConverter()
    
    #convert 100 USD to EUR
    print(converter.convert_and_format(100, "USD", "EUR"))
    
    # covert 200 GBP to JPY 
    print(converter.convert_and_format(200, "GBP", "JPY"))
    
    # convert 500 INR to USD
    print(converter.convert_and_format(500, "INR", "USD"))
    
# Example 6: Pizza Ordering

class Pizza:
    def __init__(self):
        self.base_price = 0.0
    
    def get_price(self):
        return self.base_price
    
#class for Size
class Size:
    def __init__(self, size):
        self.size = size
        self.base_price = self.calculate_base_price()
    
    def calculate_base_price(self):
        if self.size == "small":
            return 10.0
        elif self.size == "medium":
            return 15.0
        elif self.size == "large":
            return 20.0
        else: 
            raise ValueError("Invalid Size. Choose from small, medium, large")

# Derived class for Toppings
class Topping(Pizza, Size):
    def __init__(self, size, topping):
        Pizza.__init__(self) # Call the base class constructor Initialize base price
        Size.__init__(self, size) # Call the base class constructor Initialize base price
        self.topping = []
        self.topping_prices = {
            "pepperoni": 1.50,
            "mushroom": 1.00,
            "onion": 0.50,
            "sausage": 1.75,
            "extra cheese": 2.00,
            "black olives" : 1.00
        }
    def add_topping(self, topping):
        if topping in self.topping_prices:
            self.topping.append(topping)
        else:
            raise ValueError("Invalid topping. Choose from the available toppings")
    
    def get_price(self):
        total_price = self.base_price
        for topping in self.topping:
            total_price += self.topping_prices[topping]
        return total_price

if __name__ == "__main__":
    # Create a new instance of pizza
    my_pizza = Topping("medium", "pepperoni")
    
    # Add toppings
    my_pizza.add_topping("pepperoni")
    my_pizza.add_topping("mushroom")
    my_pizza.add_topping("onion")
    
    total_price = my_pizza.get_price()
    print(f"Total price: ${total_price:.2f}")
    
    
    
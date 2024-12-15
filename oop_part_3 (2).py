# -*- coding: utf-8 -*-
"""oop part 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CLl7mhltQSUhDAsu8NECaATGQ03ej3Lp
"""

class Product:
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def is_in_stock(self, quantity):
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        if self.is_in_stock(quantity):
            self.stock -= quantity

class Admin:
    def __init__(self):
        self.product = []
        self.order = []

    def add_product(self, product):
        self.product.append(product)

    def view_products(self):
        for product in self.product:
            print(f"Product Name: {product.product_name}, Price: {product.price}, Stock: {product.stock}")

    def order_history(self):
        for order in self.order:
            print(f"Customer: {order['customer']}")
            for item in order['cart']:
                print(f"  {item['product']} - {item['quantity']} @ {item['price']} each")

class Customer:
    def __init__(self, name, email, admin):
        self.name = name
        self.email = email
        self.admin = admin
        self.cart = []

    def add_to_cart(self, product_name, quantity):
        for i in self.admin.product:
            if i.product_name == product_name:
                if i.is_in_stock(quantity):
                    i.reduce_stock(quantity)
                    self.cart.append({"product": product_name, "quantity": quantity, "price": i.price})
                    print(f"Added {quantity} of {product_name} to the cart.")
                else:
                    print(f"Product {product_name} is out of stock.")
                return
        print(f"Product {product_name} not found.")

    def bill(self):
        total = 0
        print(f"Customer Name: {self.name}, Email: {self.email}")
        for item in self.cart:
            print(f"{item['product']} - {item['quantity']} @ {item['price']} each")
            total += item["price"] * item['quantity']

        print(f"Total bill: {total}")


        self.admin.order.append({"customer": self.name, "cart": self.cart})


admin = Admin()
admin.add_product(Product("Laptop", 1000, 10))
admin.add_product(Product("Mouse", 50, 30))


customer = Customer("John Doe", "john@example.com", admin)
customer.add_to_cart("Laptop", 2)
customer.add_to_cart("Mouse", 5)


customer.bill()
admin.order_history()
admin.view_products()

class BankAccount:
  def __init__(self,account_number,customer_name,balance):
    self.account_number=account_number
    self.customer_name=customer_name
    self.balance=balance

  def add_money(self,amount):
    self.balance += amount
    print(f"Money {amount} is added to your bank account successfully.")


  def withdraw_money(self,amount):
    if self.balance >= amount:
      self.balance -= amount
      return f"Money {amount} successfully withdraw."
    else:
      print("Insufficient balance.")

from datetime import datetime

class FixedDeposit(BankAccount):

  def __init__(self,parent,balance,dateofstarted,interest_rate):
    super().__init__(parent.account_number,parent.customer_name,balance)
    self.interest_rate=interest_rate
    self.dateofstarted=dateofstarted

  def calculate_interest(self):
    current_date=datetime.now()
    a=current_date.year - self.dateofstarted.year

    if (current_date.month, current_date.day) < (self.dateofstarted.month, self.dateofstarted.day):
          a-=1

    if a >=1:
        print(self.balance*(self.interest_rate/100)*a)
        print("nice")
    else:
      print("To have interest you have to pass atleast 1 year")


austin =BankAccount(123,"austin",50000)
austin.add_money(5000)
austin.withdraw_money(2000)
print(austin.balance)

fd_account = FixedDeposit(austin, 10000, datetime(2020, 12, 1), 5.0)
print(fd_account.calculate_interest())

from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Money {amount} is added to your bank account successfully. Current balance: {self.balance}"
        else:
            return "Amount must be positive."

    def withdraw_money(self, amount):
        if amount <= 0:
            return "Amount must be positive."
        if self.balance >= amount:
            self.balance -= amount
            return f"Money {amount} successfully withdrawn. Current balance: {self.balance}"
        else:
            return "Insufficient balance."


class FixedDeposit(BankAccount):
    def __init__(self, parent_account, balance, dateofstarted, interest_rate):
        super().__init__(parent_account.account_number, parent_account.customer_name, balance)
        self.dateofstarted = dateofstarted
        self.interest_rate = interest_rate

    def calculate_interest(self):
        current_date = datetime.now()
        years_elapsed = current_date.year - self.dateofstarted.year


        if (current_date.month, current_date.day) < (self.dateofstarted.month, self.dateofstarted.day):
            years_elapsed -= 1

        if years_elapsed >= 1:
            interest = self.balance * (self.interest_rate / 100) * years_elapsed
            return f"Interest for {years_elapsed} year(s) is: {interest}"
        else:
            return "To earn interest, at least 1 year must pass since the deposit started."



main_account = BankAccount(12345, "Austin Karki", 5000)


fd_account = FixedDeposit(main_account, 10000, datetime(2020, 12, 1), 5.0)


print(fd_account.account_number)
print(fd_account.customer_name)
print(fd_account.calculate_interest())

# modes= X create
# read=r
# write=w
# append =a
# a=open("file name","mode") Two time run its create error because same file cannot be 2 time as name is same
# a.close()
# pwd = to find location or home directory in jupyter notebook

try:
  print("Hello")
except:
  print("NO")

class Bus:
  def __init__(self,capacity):
    self.capacity=capacity
  def available(self,need):
    return self.capacity > need
  def decrease(self,need):
    self.capacity -= need
    return self.capacity

class Passenger:
  def __init__(self,bus):
    self.bus = bus
    self.detail=[]
  def booking(self,name,need):
    if self.bus.available(need):
      self.bus.decrease(need)
      print(f"{need} seat booked.")
      print(f"{self.bus.capacity} is still available.")


      self.detail.append(a)

class Reservation:
  def __init__(self,passenger):
    self.passenger = passenger
  def view_bookings(self):
    if not self.passenger.details:
        print("No bookings made yet.")
    else:
        print("Booking details:")
        for detail in self.passenger.details:
          print(detail)
a=Bus(25)
b=Passenger(a)
c=Reservation(b)

b.booking("Alice", 5)
b.booking("Bob", 10)
b.booking("Charlie", 40)

c.view_bookings
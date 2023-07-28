class Product:
  def __init__ (self, name, price, units):
    self.name = name
    self.price = price
    self.units = units
    self.is_on_sale = False

  def describe(self):
    display_money = "{:,.2f}".format(self.price)
    print(f"Product name: {self.name}")
    print(f"Product price: ${display_money}")
    print(f"Available units: {self.units}")
    print(f"On sale? {self.is_on_sale}")
    print(f"In stock? {self.is_in_stock()}")
    print("-------------------------")
  
  def add_units(self, units):
    if type(units) == int:
      self.units += units
    else:
      print(f"Error: {units} is not a valid entry.")
      print("-------------------------")

  def reduce_units(self, units):
    if type(units) == int:
      if self.units - units >=0:
        self.units -= units
      else:
        print("Error: Not enough units in inventory.")
        print("-------------------------")
    else:
      print(f"Error: {units} is not a valid entry.")
      print("-------------------------")
  
  def reduce_price(self, discount):
    if discount > 0 and discount < 1:
      self.price = self.price * (1 - discount)
      self.is_on_sale = True
    else:
      print(f"Error: {discount} is an invalid percentage.")
      print("-------------------------")

  def is_in_stock(self):
    if self.units > 0:
      return True
    else:
      return False

  def units_total_value(self):
    self.units_total_value = "{:,.2f}".format(self.price * self.units)
    print(f"Value of current stock of units: ${self.units_total_value}")
    print("-------------------------")

laptop = Product("Dell Laptop", 1700, 12)
laptop.describe()
laptop.add_units(5)
laptop.describe()
laptop.add_units(2.5)
laptop.describe()
laptop.reduce_units(5)
laptop.describe()
laptop.reduce_units('four')
laptop.describe()
laptop.reduce_price(0.5)
laptop.describe()
laptop.reduce_price(50)
laptop.describe()
laptop.reduce_units(12)
laptop.describe()
laptop.reduce_units(20)
laptop.describe()
laptop.add_units(100)
laptop.describe()
laptop.units_total_value()

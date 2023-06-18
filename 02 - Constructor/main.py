class Item:
  pay_rate = 0.8 # The pay rate after 20% discount
  def __init__(self, name: str, price: float, quantity=0):
    # Run validations to the received arguments
    assert price >= 0, f'Price {price} is not greater than or equal to zero!'
    assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'

    # Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity
    # print(f'An instance created: {name}')

  def calculate_total_price(self):
    return self.price * self.quantity

  def apply_discount(self):
    # Item.pay_rate is only accessible at the class level, whereas
    # self.pay_rate is accessible at instance level. Otherwise, it is accessible at class level
    self.price = self.price * self.pay_rate

item1 = Item('Phone', 100, 1)
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))
item1.apply_discount()
print(item1.price)

item2 = Item('Laptop', 1000, 3)
# item2.name = 'Laptop'
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))
# item2.has_numpad = False
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.pay_rate) # class attribute
# print(item1.pay_rate) # instance attribute
# print(item2.pay_rate) # instance attribute
item2.pay_rate = 0.7 # changes pay_rate in the instance level instead of class level
item2.apply_discount()
print(item2.price)

# use for debugging classes
# print(Item.__dict__) # returns all attributes for Class level
# print(item1.__dict__) # returns all attributes for instance level




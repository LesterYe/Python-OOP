import csv

class Item:
  pay_rate = 0.8 # The pay rate after 20% discount
  all = []
  def __init__(self, name: str, price: float, quantity=0):
    # Run validations to the received arguments
    assert price >= 0, f'Price {price} is not greater than or equal to zero!'
    assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'

    # Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity

    # Actions to execute
    Item.all.append(self)

  def calculate_total_price(self):
    return self.price * self.quantity

  def apply_discount(self):
    # Item.pay_rate is only accessible at the class level, whereas
    # self.pay_rate is accessible at instance level. Otherwise, it is accessible at class level
    self.price = self.price * self.pay_rate

  @classmethod # passes class as first argument
  def instantiate_from_csv(cls):
    with open('items.csv', 'r') as f:
      reader = csv.DictReader(f)
      items = list(reader)
    
    for item in items:
      # print(item)
      Item(
        name = item['name'], # or item.get('name')
        price = float(item['price']), # or float(item.get('price'))
        quantity = int(item['quantity']) # or int(item.get('quantity'))
      )
    # print(items)

  @staticmethod # does not pass instance as first argument
  def is_integer(num):
    # We will count out the floats that are point zero
    # e.g. 5.0, 10.0
    if isinstance(num, float):
      # is_integer() includes the floats that are point zero
      return num.is_integer() # is_integer() is a built-in function
    elif isinstance(num, int):
      return True
    else:
      return False

  def __repr__(self):
    # return f'Item("{self.name}", {self.price}, {self.quantity})'
    return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'

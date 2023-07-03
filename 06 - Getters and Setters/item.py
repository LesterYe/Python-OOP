import csv

class Item:
  pay_rate = 0.8 # The pay rate after 20% discount
  all = []
  def __init__(self, name: str, price: float, quantity=0):
    # Run validations to the received arguments
    assert price >= 0, f'Price {price} is not greater than or equal to zero!'
    assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'

    # Assign to self object
    self._name = name # single underscore is pythonic way for us to set a property as an assignable attribute.
    # Otherwise, self.name cannot be set because name is already a property
    # We need to set self._name under the property decorator too.
    # Therefore, self._name is writable but self.name is read-only
    # self.__name # a double-underscored attribute that is entirely inaccessible outside of the class
    # aka private keys
    self.price = price
    self.quantity = quantity

    # Actions to execute
    Item.all.append(self)

  @property
  # Property Decorator = Read-Only Attribute
  def name(self):
    # print('You are trying to get name')
    return self._name
  
  @name.setter
  # changes a read-only attribute to a settable attribute
  # we should always receive a paramter in the setter,
  # because the value that is assigned in main.py becomes the argument in the setter.
  # With setters, we can implement if-else conditions or raise exceptions if we don't like the value that we receive
  def name(self, value):
    # print('You are trying to set name')
    self._name = value
    # if len(value) > 20:
    #   raise Exception('The name is too long!')
    # else:
    #   self._name = value

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

  # @property # decorator for read only attributes aka properties
  # def read_only_name(self):
  #   return 'AAA'
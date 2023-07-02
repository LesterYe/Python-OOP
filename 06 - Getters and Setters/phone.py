import csv
from item import Item

class Phone(Item):
  # all = [] # this is inherited by Item
  def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
    # Call to super function to have access to all attributes/methods
    # , including class attributes/methods
    super().__init__(
      name, price, quantity
    )
    
    # # Run validations to the received arguments
    # assert price >= 0, f'Price {price} is not greater than or equal to zero!'
    # assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
    assert broken_phones >= 0, f'Broken Phones {broken_phones} is not greater than or equal to zero!'

    # # Assign to self object
    # self.name = name
    # self.price = price
    # self.quantity = quantity
    self.broken_phones = broken_phones

    # # Actions to execute
    # Phone.all.append(self)

  def __repr__(self):
    # return f'Item("{self.name}", {self.price}, {self.quantity})'
    return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity}, {self.broken_phones})'

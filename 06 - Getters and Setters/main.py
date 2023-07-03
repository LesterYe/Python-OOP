# main.py will only instantiate instances

from item import Item
from phone import Phone

# Item.instantiate_from_csv()

item1 = Item('MyItem', 750)
# item1.name = 'OtherItem'

# print(Item.all)
# print(item1.read_only_name) # this is termed a property instead of an attribute
# item1.read_only_name = 'BBB'

# print(item1.__name) 
# double-underscore item1.__name will show that no attribute does not exist at all
# aka private keys

# print(item1._name)

# Setting an Attribute
item1.name = 'OtherItem' # item1.name is now both read-only and settable.

# Getting an Attribute
print(item1.name)


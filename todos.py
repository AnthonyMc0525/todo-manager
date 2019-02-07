from item import Item
from manager import Manager
import datetime

manager = Manager()

print("""
what would you like to do?
1: view list
2: add to list
3: change item to complete
""")

to_do = int(input('> '))

if to_do == 1:
    manager.print_list()
    
elif to_do == 2:
    choice = input('what would the task be called? ')
    choice_item = Item(choice)
    manager.add_to_list(choice_item)

elif to_do == 3:
    complete = input('which item would you like to change? ')
    manager.print_list()
    manager.complete_item(complete)
    

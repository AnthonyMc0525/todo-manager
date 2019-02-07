from item import Item
from manager import Manager
import datetime

do_homework = Item('do homework',datetime.datetime.now())

manager = Manager()

manager.add_to_list(do_homework)
manager.print_list()

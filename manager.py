import sys
from item import Item

script, file_name = sys.argv

class Manager(object):
    def __init__(self):
            pass

    def print_list(self):
        target = open(file_name, 'r')
        print(target.read())
        target.close()
        

    def add_to_list(self, item):
        target = open(file_name, 'a+')
        target.write(item.task)
        target.write('  '  + str(item.complete))
        target.write('  ' + str(item.timestamp) + '\n')
        target.close()

    def complete_item(self, item):

        target = open("todos.txt", "r+")
        target_list = target.readlines()

        index = 0
        self.replace_list()

    def remove_item(self, item):
        target = open("todos.txt", "w")
        target_list = target.readlines()
        target.close()
        index = 1

        replace_list()


    def run_app(self):
        choice = ''
        while choice != 5:
            print("""
            what would you like to do?
            1: view list
            2: add to list
            3: change item to complete
            5: quit
            """)
            choice = int(input('> '))

            if choice == 1:
                manager.print_list()
                
            elif choice == 2:
                choice = input('what would the task be called? ')
                choice_item = Item(choice)
                manager.add_to_list(choice_item)

            elif choice == 3:
                manager.print_list()
                complete = input('which item would you like to change? ')
                manager.complete_item(complete)
                
            elif choice == 5:
                break

manager = Manager()

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
        document_list = target.readlines()

        index = 0
        for line in document_list:
            if item in line:
                contents = line.split("  ")
                if contents[1] == "False":
                    contents[1] = 'True'
                    document_list[index] = f"{contents[0]} {contents[1]} {contents[2]}"
                    break

            index += 1
        else:
            print('you have already completed it or the item is not in the list. Please check the list to confirm')

        target.truncate(0)

        for line in document_list:
            target.write(line)

        target.close()


    def run_app(self):
        choice = ''
        while choice != 4:
            print("""
            what would you like to do?
            1: view list
            2: add to list
            3: change item to complete
            4: quit
            """)
            choice = int(input('> '))

            if choice == 1:
                Manager().print_list()
                
            elif choice == 2:
                choice = input('what would the task be called? ')
                choice_item = Item(choice)
                manager.add_to_list(choice_item)

            elif choice == 3:
                manager.print_list()
                complete = input('which item would you like to change? ')
                manager.complete_item(complete)

manager = Manager()

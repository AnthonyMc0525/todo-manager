from sys import argv

script, file_name = argv

class Manager(object):
    def print_list(self):
        target = open(file_name, 'r')
        print(target.read())
        target.close()
        

    def add_to_list(self, item):
        target = open(file_name, 'w')
        target.write(item.task)
        target.write('  '  + str(item.complete))
        target.write('  ' + str(item.timestamp))
        target.close()

    def remove_from_list(self, item):
        pass

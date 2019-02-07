import sys

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
        for line in target_list:
            if item in line:
                contents = line.split("  ")
                if tcontents[1] == "False":
                    contents[1] = 'True'
                    target_list[index] = f"{contents[0]} {contents[1]} {contents[2]}"
                    
                    break

            index += 1
        else:
            print("proccess could not be complete")

        target.truncate(0)

        for line in target_list:
            target.write(line)

        target.close()

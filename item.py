import datetime

class Item(object):
    def __init__(self, task):
        self.task = task
        self.complete = False
        self.timestamp = datetime.datetime.now()

class Item(object):
    def __init__(self, task, timestamp):
        self.task = task
        self.complete = False
        self.timestamp = timestamp

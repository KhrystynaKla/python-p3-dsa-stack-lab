class Stack:

    def __init__(self, items = [], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items)<=self.limit:
            if len(self.items)==0:
                return True
            else:
                return False

    def push(self, item):
        if len(self.items)<=self.limit:
            self.items.append(item)

    def pop(self):
        if (len(self.items) > 0):
            return self.items.pop()

    def peek(self):
        if (len(self.items)>0):
            return self.items[0]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items[(self.items.index(target)):])-1
        else:
            return -1

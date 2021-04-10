class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not len(self.items) == 0:
            return self.items[-1]

    def get_all(self):
        return self.items


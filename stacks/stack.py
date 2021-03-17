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

users = Stack()
users.push("Jordan")
users.push("Tiffany")
users.push("Kristine")

print(users.get_all())

removed_user = users.pop()

print(removed_user)

last_user = users.peek()

print(last_user)

print(users.get_all())

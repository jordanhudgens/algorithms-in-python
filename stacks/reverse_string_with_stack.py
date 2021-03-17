from stack import Stack

def reverse_string(val):
    stack = Stack()

    for char in range(len(val)):
        stack.push(val[char])

    updated_str = ""

    while not (len(stack.get_all()) == 0):
      updated_str += stack.pop()

    return updated_str

name = "Jordan"

print(reverse_string(name))

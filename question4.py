# Make a detail coding for stack (push, pop, peep(first pocket when pop function is called), display).

class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        self.items.pop(-1)

    def peep(self):
        print(self.items[-1])
    
    def display(self):
        print(self.items)

stack = Stack()
stack.push(1)
stack.push(18)
stack.push(32)
stack.display()
stack.peep()
stack.pop()
stack.peep()
stack.display()
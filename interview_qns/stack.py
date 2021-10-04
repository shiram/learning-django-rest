class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            return ("No Element in the Stack")
        else:
            return self.stack.pop()

stack1 = Stack()
stack1.add("Mon")
stack1.add("Tue")

print(stack1.remove())
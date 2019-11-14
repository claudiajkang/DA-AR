class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        val = self.items.pop()
        if val is not None:
            return val
        else:
            print("Stack is empty")

    def peak(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

    def empty(self):
        return not bool(self.items)

stack = Stack()
print("Is stack empty? : "+str(stack.empty()))

for i in range(10):
    stack.push(i)

print("Stack size : "+str(stack.size()))
print("peak : " + str(stack.peak()))
print("pop : " + str(stack.pop()))

print("Is stack empty? : "+str(stack.empty()))

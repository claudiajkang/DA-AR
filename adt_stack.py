class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def empty(self):
        if self.size() == 0:
            return True

        return False

stack = Stack()
print("Is stack empty? : "+str(stack.empty()))

for i in range(10):
    stack.push(i)

print("Stack size : "+str(stack.size()))
print("peak : " + str(stack.peak()))
print("pop : " + str(stack.pop()))

print("Is stack empty? : "+str(stack.empty()))

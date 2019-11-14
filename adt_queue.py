class Queue:
    def __init__(self):
        self.items = list()
        
    def enqueue(self, val):
        self.items.append(val)
        
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peak(self):
        if self.items:
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

    def empty(self):
        return not bool(self.items)

q = Queue()
print("Is queue empty? : "+str(q.empty()))

for i in range(10):
    q.enqueue(i)

print("queue size : "+str(q.size()))
print("peak : " + str(q.peak()))
print("dequeue : " + str(q.dequeue()))
print("peak : " + str(q.peak()))

print("Is queue empty? : "+str(q.empty()))


from sys import stdin
read = lambda: stdin.readline().rstrip()


class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add(self, data, index):
        nnode = Node(data, index)

        if not self.head:
            self.head = nnode
            self.tail = nnode

        else:
            self.tail.next = nnode

        nnode.prev = self.tail
        self.tail = nnode
        self.tail.next = self.head
        self.head.prev = self.tail

    def findleft(self, val):
        p = self.head

        for i in range(val):
            p = p.prev

            if p.index == self.head.index:
                p = p.prev

        self.delete()
        self.head = p
        self.tail = p.prev


    def findright(self, val):
        p = self.head

        for i in range(val):
            p = p.next

            if p.index == self.head.index:
                p = p.next

        self.delete()
        self.head = p
        self.tail = p.prev


    def find(self, val, init=False):
        if not init:
            if val < 0:
                self.findleft(val*(-1))

            else:
                self.findright(val)

        v = self.head.data
        idx = self.head.index

        return idx, v

    def delete(self):
        p = self.head

        self.head = p.next
        self.tail.next = self.head
        self.head.prev = self.tail


n = int(read())
arr = [0] + list(map(int, read().split()))
ll = LinkedList()

for i in range(1, n+1):
    ll.add(arr[i], i)


idx = 0
val = 0
c = 0

while c != n:
    if val == 0:
        idx, val = ll.find(1, init=True)
    else:
        idx, val = ll.find(val)
    print(idx, end = " ")
    c += 1


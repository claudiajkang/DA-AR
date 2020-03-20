from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, k):
        self.head = None
        self.tail = None
        self.k = k
        self.s = 0

    def add(self, data):
        nnode = Node(data)

        if not self.head:
            self.head = nnode

        else:
            self.tail.next = nnode

        self.tail = nnode
        self.tail.next = self.head
        self.s += 1

    def find(self):
        p = self.tail
        c = self.tail

        for i in range(self.k):
            p = c
            c = p.next

        tv = c.data

        if self.head.data == c.data:
            self.head = p.next

        self.tail = p.next
        p.next = c.next
        self.s -= 1

        return str(tv)

    def size(self):
        return self.s

n, k = map(int, stdin.readline().rstrip().split())
ll = LinkedList(k)
res = []

for i in range(1, n+1):
    ll.add(i)

while ll.size() > 0:
    res.append(ll.find())

if n > 0:
    print("<"+", ".join(res)+">")
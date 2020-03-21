from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, k):
        self.head = None
        self.tail = None
        self.k = k - 1

    def add(self, data):
        nnode = Node(data)

        if not self.head:
            self.head = nnode
            self.tail = nnode

        else:
            self.tail.next = nnode

        self.tail = nnode
        self.tail.next = self.head

    def find(self):
        p = self.head
        c = self.head

        for i in range(self.k):
            p = c
            c = c.next

        p.next = c.next
        self.tail = p
        self.head = c.next

        return c.data


n, k = map(int, stdin.readline().rstrip().split())
ll = LinkedList(k)

if n > 0:
    for i in range(1, n+1):
        ll.add(i)

    print("<", end="")
    for i in range(n):
        print(ll.find(), end = "")
        if i != n-1:
            print(", ", end ="")
    print(">")

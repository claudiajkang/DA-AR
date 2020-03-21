from sys import stdin
read = lambda: stdin.readline().rstrip()

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add(self, data):
        nnode = Node(data)

        if not self.head:
            self.head = nnode
            self.tail = nnode

        else:
            self.tail.next = nnode
            nnode.prev = self.tail

        self.tail = nnode
        self.tail.next = self.head
        self.head.prev = self.tail

    def equal(self, data):
        if self.head.data == data:
            return True
        return False


    def left(self, data):
        p = self.head.prev
        c = 1

        while p.data != data:
            c += 1
            p = p.prev

        return p, c

    def right(self, data):
        p = self.head.next
        c = 1

        while p.data != data:
            c += 1
            p = p.next

        return p, c

    def delete(self):
        p = self.head.next
        self.head = p
        self.head.prev = self.tail
        self.tail.next = p

    def find(self, data):
        if not self.equal(data):
            lp, cl = self.left(data)
            rp, cr = self.right(data)

            if cl < cr:
                self.head = lp
                self.tail = self.head.prev
                c = cl
            else:
                self.head = rp
                self.tail = self.head.prev
                c = cr
        else:
            c = 0

        self.delete()
        return c

n, m = map(int, read().split())
q = list(map(int, read().split()))
ll = LinkedList()

for i in range(1, n+1):
    ll.add(i)

res = 0
for i in q:
    res += ll.find(i)

print(res)

from sys import stdin

read = lambda: stdin.readline().rstrip()


class Node:
    def __init__(self, data):
        self.data = data
        self.before = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            new_node.before = self.tail
            self.tail.next = new_node

        self.tail = new_node
        self.head.before = self.tail


    def equal(self, val):
        if self.head.data == val:
            return True
        return False

    def left(self, val):
        p = self.head
        c = 0

        while p.data != val:
            p = p.before
            c += 1

        return c

    def right(self, val):
        p = self.head
        c = 0

        while p.data != val:
            p = p.next
            c += 1

        return c

    def set_head(self, val):
        if self.head.data != val:
            p = self.head
            c = self.head.next

            while c.data != val:
                p = c
                c = p.next

            self.tail.next = self.head
            self.head = c
            self.tail = p
            self.tail.next = None

    def delete(self, val):
        if self.head.data == val:
            nnode = self.head.next
            self.head = nnode
            self.tail.next = nnode
            if self.head != None:
                self.head.before = self.tail

        else:
            p = self.head
            c = self.head.next

            while c.data != val:
                p = c
                c = p.next

            nnode = c.next
            p.next = nnode
            nnode.before = p


n, m = map(int, read().split())
lo = list(map(int, read().split()))
ll = LinkedList()
c = 0

for i in range(1, n+1):
    ll.add(i)

while lo:
    v = lo.pop(0)

    if ll.equal(v):
        ll.delete(v)
        continue

    l = ll.left(v)
    r = ll.right(v)

    if l > r:
        c += r

    else:
        c += l

    ll.set_head(v)
    ll.delete(v)


print(c)
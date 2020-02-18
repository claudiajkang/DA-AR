from sys import stdin

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self ):
        self.head = Node('head')
        self.tail = self.head

    def add(self, data):
        nnode = Node(data)
        nnode.next = self.head.next
        self.tail.next = nnode
        self.tail = nnode

def main():
    N, K = map(int, stdin.readline().strip().split())
    LL = LinkedList()

    for i in range(1, N+1):
        LL.add(i)

    p = LL.head
    res = []
    F = 0

    while len(res) < N:
        for i in range(K-1):
            p = p.next

        dnode = p.next
        if str(dnode.data) not in res:
            res.append(str(dnode.data))
            p.next = dnode.next
        else:
            res.append(str(dnode.next.data))
            p.next = dnode.next.next

    print('<'+', '.join(res)+'>')

main()

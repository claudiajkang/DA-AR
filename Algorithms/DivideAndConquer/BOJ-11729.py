from sys import stdin

def hanoi(n, a1, a2, a3):
    global move

    if n == 1:
        move.append([a1, a3])
    else:
        hanoi(n-1, a1, a3, a2)
        move.append([a1, a3])
        hanoi(n-1, a2, a1, a3)


move = []
n = int(stdin.readline().rstrip())
hanoi(n, 1, 2, 3)

print(len(move))
for i, j in move:
    print("%d %d" % (i, j))

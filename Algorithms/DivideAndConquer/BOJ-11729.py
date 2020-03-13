from sys import stdin

def hanoi(n, a, b, c):
    global move
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)

move = []
n = int(stdin.readline().rstrip())
hanoi(n, 1, 2, 3)

print(len(move))
for i, j in move:
    print("%d %d" % (i, j))

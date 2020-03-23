from sys import stdin
read = lambda: stdin.readline().rstrip()

t = int(read())
word = [read() for i in range(t)]

for _ in range(t):
    l = []
    r = []

    for w in word[_]:
        if w == "<":
            if l: r.append(l.pop())
        elif w == ">":
            if r: l.append(r.pop())
        elif w == '-':
            if l: l.pop()
        else:
            l.append(w)

    print(''.join(l) + ''.join(reversed(r)))
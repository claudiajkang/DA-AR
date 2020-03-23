from sys import stdin
read = lambda: stdin.readline().rstrip()

t = int(read())

for _ in range(t):
    s = read()
    l = []
    r = []

    for i in range(len(s)):
        if s[i] == '<':
            if l: r.append(l.pop())

        elif s[i] == '>':
            if r: l.append(r.pop())

        elif s[i] == '-':
            if l: l.pop()

        else:
            l.append(s[i])

    print(''.join(l) + ''.join(reversed(r)))


from sys import stdin

l = list(stdin.readline().strip())
r = []
N = int(stdin.readline())

for line in stdin:
    if line[0] == 'L':
        if l: r.append(l.pop())
    elif line[0] == 'D':
        if r: l.append(r.pop())
    elif line[0] == 'B':
        if l:
            v = l.pop()
    elif line[0] == 'P':
        l.append(line[2])

print(''.join(l)+''.join(reversed(r)))

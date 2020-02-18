from sys import stdin
  
L = list(stdin.readline().strip())
N = int(stdin.readline())
R = []

for line in stdin: 
    if line[0] == 'L':
        if L: R.append(L.pop())
    elif line[0] == 'D':
        if R: L.append(R.pop())
    elif line[0] == 'B':
        if L: L.pop()
    elif line[0] == 'P':
        L.append(line[2])

print(''.join(L)+''.join(reversed(R)))

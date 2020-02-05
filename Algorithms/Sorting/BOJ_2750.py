N = int(input())
l = list()

for i in range(N):
    v = int(input())
    l.append(v)

l = sorted(l)

for i in range(N):
    print(l[i])

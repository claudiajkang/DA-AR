t = input().split()
n, d = int(t[0]), int(t[1])

arr = input().split()
tarr = list()


for i in range(d):
    t = arr.pop(0)
    tarr.append(t)


for a in arr:
    print(a, end=' ')

for ta in tarr:
    print(ta, end=' ')
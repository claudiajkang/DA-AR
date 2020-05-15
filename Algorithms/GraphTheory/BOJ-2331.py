from sys import stdin

read = lambda: stdin.readline().rstrip()

a, p = read().split()
p = int(p)
arr = [a]

while True:
    r = 0
    for a in arr[-1]:
        r += int(a) ** p
    if str(r) in arr:
        tidx = arr.index(str(r))
        print(len(arr[:tidx]))
        break
    else:
        arr.append(str(r))

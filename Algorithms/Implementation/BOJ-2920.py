from sys import stdin

l = list(map(int, stdin.readline().rstrip().split()))
asc = 1
dsc = 8

for i in l:
    if i == asc:
        asc += 1

    if i == dsc:
        dsc -= 1

if asc == 9:
    print('ascending')

elif dsc == 0:
    print('descending')

else:
    print('mixed')

import sys
  
n = int(sys.stdin.readline())
m = 1001
res = [0 for i in range(m)]

for i in range(1, n+1):
    if i == 1:
        res[i] = 1
    elif i == 2:
        res[i] = 2
    elif i == 3:
        res[i] = 3
    elif i == 4:
        res[i] = 5
    else:
        res[i] = res[i-1] + res[i-2]

print(res[n]%10007)

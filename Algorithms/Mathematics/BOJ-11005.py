import sys
  
N, B = map(int, sys.stdin.readline().split())
res = ''

while N > 0:
    N, R = divmod(N, B)
    if R > 9: res = chr(55+R) + res
    else: res = str(R) + res

print(res)

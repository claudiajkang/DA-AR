from sys import stdin
  
def gcd(a, b):
    if b:
        return gcd(b, a%b)
    return a

A, B = map(int, stdin.readline().strip().split())
m = 11111111
g = gcd(A,B)

if g > m:
    print(m)
else:
    print('1'*g)

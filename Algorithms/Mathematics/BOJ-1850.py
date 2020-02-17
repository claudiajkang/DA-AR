from sys import stdin

def gcd(a,b):
    if b:
        return gcd(b, a%b)
    return a

N = stdin.readline().split()

r = '1'*gcd(int(N[0]), int(N[1]))
print(r)

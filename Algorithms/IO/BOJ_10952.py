import sys
  
for i in sys.stdin:
    a, b = map(int, i.split())
    if a == 0 and b == 0:
        break
    print(a+b)


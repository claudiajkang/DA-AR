import sys
  
v = sys.stdin.readline().replace('\n','')

c = int(len(v)/10) + 1

for i in range(c):
    print(v[i*10:i*10+10])

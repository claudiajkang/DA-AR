import sys
  
w = sys.stdin.readline().replace('\n','')

for i in range(len(w)):
    print(w[i*10:i*10+10])

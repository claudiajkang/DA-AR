import sys

N = int(sys.stdin.readline())
if not N:
    sys.stdout.write('0')
    exit()
res = ''

while N:
    if N % (-2):
        res = '1' + res
        N = N//-2 + 1
    else:
        res = '0' + res
        N //= -2
        
sys.stdout.write(res)


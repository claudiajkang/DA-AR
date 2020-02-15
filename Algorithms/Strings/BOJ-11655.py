from sys import stdin

s = stdin.readline().replace('\n','')
lo = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmn'
up = lo.upper()
res = ''

for i in s:
        if i in lo:
                idx = lo.find(i)
                res += lo[idx+13]
        elif i in up:
                idx = up.find(i)
                res += up[idx+13]
        else:
                res += i

print(res)
    

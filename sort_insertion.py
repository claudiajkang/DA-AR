def insertion(l):
    for i in range(0, len(l)):
        t = i
        print("++++")
        print(i)
        for j in range(i+1, len(l)):
            if l[t] > l[j]:
                l.insert(t, l[j])
                del l[j+1] 
        print(l)

tl = [11,3,28,43,9,4]
print(tl)
insertion(tl)
print(tl)

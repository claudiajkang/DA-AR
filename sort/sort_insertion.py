def insertion(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -=1

tl = [11,3,28,43,9,4]
print(tl)
insertion(tl)
print(tl)

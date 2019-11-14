def bubble(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

                print("----")
                print(i) 
                print(l)

tlist = [11,3,28,43,9,4]
print(tlist)
print("---")
bubble(tlist)
print("---")
print(tlist)

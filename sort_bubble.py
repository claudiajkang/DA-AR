def bubble(l):
    for i in range(0, len(l)):
        for j in range(0, len(l)-1):
            if l[j] > l[j+1]:
                t = l[j]
                l[j] = l[j+1]
                l[j+1] = t
           
                print("----")
                print(i) 
                print(l)

tlist = [11,3,28,43,9,4]
print(tlist)
print("---")
bubble(tlist)
print("---")
print(tlist)

def gnome(l):
    for i in range(0, len(l)-1):
        print("+++")
        t=i
        for j in range(i+1, -1, -1):
            if t < j and l[t] > l[j] and t>-1:
                l[t], l[j] = l[j], l[t]
                print(l)

                if t == j-1:
                    t = j-2

temp = [5,3,2,4]
print("---")
print(temp)
gnome(temp)
print("---")
print(temp)




def selection(l):
    for i in range(0, len(l)):
        temp = i
        for j in range(i, len(l)):
            if l[temp] > l[j]:
                temp = j

        l[i], l[temp] = l[temp], l[i]
        print("++++++")
        print(i)
        print(l)


tl = [11,3,28,43,9,4]
print(tl)
selection(tl)
print(tl)

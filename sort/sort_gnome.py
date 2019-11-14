def gnome(l):
    i = 0
    while i<=len(l):
        if i==0 or l[i-1] <= l[i]:
            i=i+1
        else:
            l[i-1], l[i] = l[i], l[i-1]
            i=i-1
        
temp = [5,3,2,4]
print("---")
print(temp)
gnome(temp)
print("---")
print(temp)

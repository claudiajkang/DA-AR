def quick(olist):
    if len(olist) > 1:
        pi, res = qsort(olist)

        if pi == 0:
            pivot = [res.pop(0)]
            right = quick(res)
            return pivot + right

        elif pi > 1:
            left = quick(olist[:pi])
            pivot = [olist[pi]]
            right = quick(olist[pi+1:])
            return left + pivot + right

    return olist


def qsort(olist):
    length = len(olist)
    pivot = 0
    l, r = 1, length - 1

    while True:
        for i in range(l, length):
            if olist[i] > olist[pivot]:
                l = i
                break
            elif i == (length-1):
                l = -1
                break

        for j in range(r, -1, -1):
            if olist[j] < olist[pivot]:
                r = j
                break

            elif j == 0:
                r = -1
                break

        if l == -1 or r == -1:
            if olist[0] > olist[r] and r > 0:
                olist[0], olist[r] = olist[r], olist[0]
            break

        elif l < r and olist[l] > olist[r]:
            olist[l], olist[r] = olist[r], olist[l]
            l = l + 1
            r = r - 1

        elif l > r and olist[l] > olist[r]:
            temp = olist[pivot]
            olist[pivot] = olist[r]
            olist[r] = temp
            pivot = r
            break

    return pivot, olist


plist = [5, 2, 8, 9, 1, 7, 3, 4, 6]
res = quick(plist)
print(res)
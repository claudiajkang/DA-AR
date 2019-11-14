def binarysearch(olist, val):
    start = 0
    end = len(olist)
    mid = int(end / 2)

    while True:
        if start == end and olist[mid] != val:
            mid = None
            break

        elif olist[mid] == val:
            break

        elif olist[mid] < val:
            start = mid + 1
            mid = int((start + end) / 2)

        elif olist[mid] > val:
            end = mid - 1
            mid = int((start + end) / 2)

    return mid


def resprint(res, val):
    if res is None:
        print(str(val) + ": X")

    else:
        print(str(val) + ": O")


plist = [1, 2, 5, 6, 7, 10, 12, 14, 15]
val = 12
res = binarysearch(plist, 12)
resprint(res, 12)
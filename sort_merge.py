# 이미 두 개의 배열이 정렬되어 진 경우


def divide(olist):
    mid = int(len(olist) / 2)
    if mid >= 1:
        left = divide(olist[:mid])
        right = divide(olist[mid:])
        res = merge(left, right)
        return res

    else:
        return olist

def merge(left, right):
    res = []
    lv = left[0]
    rv = right[0]

    while True:
        if lv is None:
            for i in right:
                res.append(i)
            break

        elif rv is None:
            for i in left:
                res.append(i)
            break

        elif lv >= rv:
            rv = right.pop(0)
            res.append(rv)

            if len(right) > 0:
                rv = right[0]

            else:
                rv = None

        elif lv < rv:
            lv = left.pop(0)
            res.append(lv)

            if len(left) > 0:
                lv = left[0]

            else:
                lv = None

    return res


t = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
r = divide(t)
print(r)
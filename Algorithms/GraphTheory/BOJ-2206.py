
while q:
    qsize = len(q)
    time += 1

    for i in range(qsize):
        crash, ch, cw = q.popleft()

        if ch == (h - 1) and cw == (w - 1):
            suc = True
            break

        for hh, ww in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            th = hh + ch
            tw = ww + cw

            if 0 < th or th >= h or 0 < tw or tw >= w: continue

            if visited[crash][th][tw]: continue

            if g[th][tw] and crash:
                continue

            elif g[th][tw] and not crash:
                visited[1][th][tw] = True
                q.append([1, th, tw])

            else:
                visited[crash][th][tw] = True
                q.append([crash, th, tw])

    if suc: break

if suc:
    print(time)
else:
    print(-1)

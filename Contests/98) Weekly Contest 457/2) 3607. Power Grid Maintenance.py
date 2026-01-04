"""
https://leetcode.com/problems/power-grid-maintenance
"""


def processQueries(
    c: int, connections: list[list[int]], queries: list[list[int]]
) -> list[int]:
    """"""

    # Union Find / Disjoint Set (https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

    # 0) I don't think it can be done without UF/DS. I tried:

    # 0.1) Without Heap:

    """
    ans = []

    hm2 = {}
    hm = {}

    for u, v in sorted(connections):
        u, v = sorted([u, v])
        if u not in hm2 and v not in hm2:
            hm[u] = [u, v]
            hm2[v] = u
            hm2[u] = u
        else:
            try:
                hm[hm2[u]].append(v)
                hm2[v] = hm2[u]
            except KeyError:
                hm[hm2[v]].append(u)
                hm2[u] = hm2[v]

    print(hm)
    print(hm2)

    offline = set()

    for t, x in queries:
        if t == 1:
            if x in offline:
                mn = float("inf")
                for st in hm[hm2[x]] if x in hm2 else [x]:
                    if st not in offline:
                        mn = min(mn, st)
                ans.append(-1 if mn == float("inf") else mn)
            else:
                ans.append(x)
        elif t == 2:
            offline.add(x)

    return ans
    """

    # 0.2) With Heap:

    """
    from heapq import heapify, heappush, heappop

    hm = {}
    hl = []  # heap list
    i = 0
    for u, v in sorted((min(u, v), max(u, v)) for u, v in connections):
        print(u, v)
        if u not in hm and v not in hm:
            hm[u] = hm[v] = i
            hl.append([u, v])
            heapify(hl[-1])
            i += 1
        elif u in hm:
            hm[v] = hm[u]
            heappush(hl[hm[u]], v)
        elif v in hm:
            hm[u] = hm[v]
            heappush(hl[hm[v]], u)

    print(hm, hl)

    res = []
    off = set()

    for t, x in queries:
        if t == 1:
            if x not in off:
                res.append(x)
            else:
                if x not in hm:
                    res.append(-1)
                else:
                    i = hm[x]
                    flag = False
                    while hl[i]:
                        mn = hl[i][0]
                        if mn in off:
                            heappop(hl[i])
                        else:
                            res.append(mn)
                            flag = True
                            break
                    if flag == False:
                        res.append(-1)
        if t == 2:
            off.add(x)

    return res
    """

    pass

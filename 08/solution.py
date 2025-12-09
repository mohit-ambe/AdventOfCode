from heapq import heappush, heappop
from collections import Counter

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

coords = [tuple(map(int, line.split(","))) for line in myin]
dist = lambda a, b:sum([(d1 - d2) ** 2 for d1, d2 in zip(a, b)])

queue = []
parents = dict()
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        c1, c2 = coords[i], coords[j]
        d = dist(c1, c2)
        if d != 0:
            heappush(queue, (d, i, j))
    parents[i] = i


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        parents[ry] = rx


def part_one():
    Q = queue.copy()
    P = parents.copy()

    for _ in range(1000):
        _, a, b = heappop(Q)
        if find(a) != find(b):
            union(a, b)

    counts = None
    while counts != Counter(P.values()):
        counts = Counter(P.values())
        P = {k:find(P[k]) for k in P}

    sizes = sorted(counts.values())
    print(sizes[-1] * sizes[-2] * sizes[-3])


def part_two():
    Q = queue.copy()
    x1, x2 = 0, 0

    while Q:
        _, a, b = heappop(Q)
        if find(a) != find(b):
            union(a, b)
            x1, x2 = coords[a][0], coords[b][0]

    print(x1 * x2)


part_one()
part_two()

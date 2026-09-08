import heapq
import random

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

adj = dict()
edges = dict()
for line in myin:
    key, vals = line.split(": ")
    for val in vals.split(" "):
        adj[key] = adj.get(key, []) + [val]
        adj[val] = adj.get(val, []) + [key]
        edges[(key, val)] = 0


def bfs(start, target):
    Q = [(0, start)]
    visited = {start}
    prev = {}

    while Q:
        weight, node = heapq.heappop(Q)
        if node == target:
            break
        for neighbor in adj[node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            prev[neighbor] = node
            heapq.heappush(Q, (weight + 1, neighbor))

    node = target
    while node != start:
        previous = prev[node]
        if (previous, node) in edges:
            edges[(previous, node)] += 1
        else:
            edges[(node, previous)] += 1
        node = previous


def neighbors(start):
    seen = set()
    Q = [start]
    while Q:
        node = Q.pop()
        if node in seen:
            continue
        seen.add(node)
        Q.extend(adj[node])
    return seen


def part_one():
    c1, c2 = "", ""
    for _ in range(3):
        nodes = list(adj.keys())
        for _ in range(50):
            a, b = random.choices(nodes, k=2)
            bfs(a, b)

        cut = sorted(edges.items(), key=lambda x: x[1], reverse=True)[0][0]
        c1, c2 = cut
        adj[c1].remove(c2)
        adj[c2].remove(c1)

    print(len(neighbors(c1)) * len(neighbors(c2)))


part_one()
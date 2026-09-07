file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

map = [[*line] for line in myin]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

R = len(map)
C = len(map[0])

start = (0, 1)
end = (R - 1, C - 1 - 1)


def part_one():
    Q = [(start, (0, 0), 0)]
    dist = 0
    while Q:
        curr, prev, d = Q.pop(0)
        y, x = curr
        if curr == end:
            dist = max(dist, d)
        for dy, dx in directions:
            if (y + dy, x + dx) == prev:
                continue
            if not 0 <= y + dy < R or not 0 <= x + dx < C:
                continue
            if map[y + dy][x + dx] == "#":
                continue
            if (dy, dx) == (-1, 0) and map[y + dy][x + dx] == "v":
                continue
            if (dy, dx) == (0, -1) and map[y + dy][x + dx] == ">":
                continue
            Q.append(((y + dy, x + dx), curr, d + 1))
    print(dist)


def part_two():
    # find vertices
    forks = {start, end}
    Q = [start]
    visited = set()

    while Q:
        curr = Q.pop(0)
        y, x = curr
        if curr in visited:
            continue
        visited.add(curr)

        valid = 0
        for dy, dx in directions:
            if not 0 <= y + dy < R or not 0 <= x + dx < C:
                continue
            if map[y + dy][x + dx] == "#":
                continue
            Q.append((y + dy, x + dx))
            valid += 1

        if valid > 2:
            forks.add(curr)

    # make adjacency graph and distances between vertices
    adj = dict()
    dist = dict()
    for fork in forks:
        Q = [(fork, fork, 0)]
        visited = set()
        while Q:
            curr, prev_fork, d = Q.pop(0)
            y, x = curr
            if curr in visited:
                continue
            visited.add(curr)

            if prev_fork != curr and curr in forks:
                adj[prev_fork] = adj.get(prev_fork, set()) | {curr}
                adj[curr] = adj.get(curr, set()) | {prev_fork}
                dist[(prev_fork, curr)] = d
                dist[(curr, prev_fork)] = d
                continue

            for dy, dx in directions:
                if not 0 <= y + dy < R or not 0 <= x + dx < C:
                    continue
                if map[y + dy][x + dx] == "#":
                    continue
                Q.append(((y + dy, x + dx), prev_fork, d + 1))

    max_dist = 0
    visited = set()

    # backtracking dfs
    def dfs(u, curr_dist):
        nonlocal max_dist
        if u == end:
            max_dist = max(max_dist, curr_dist)
            return

        visited.add(u)
        for v in adj.get(u, set()):
            if v not in visited:
                dfs(v, curr_dist + dist[(u, v)])
        visited.remove(u)

    dfs(start, 0)
    print(max_dist)


part_one()
part_two()
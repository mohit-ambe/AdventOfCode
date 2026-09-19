from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

start = (-1, 0)
end = (len(myin) - 2, len(myin[-1]) - 3)
R, C = len(myin) - 2, len(myin[0]) - 2
valid = {start, end}
obs = {d: set() for d in "<v>^"}
directions = {
    "<": (0, -1),
    "v": (1,  0),
    ">": (0,  1),
    "^": (-1, 0)
}

for i, line in enumerate(myin[1:]):
    for j, char in enumerate(line[1:]):
        if char != "#":
            valid.add((i, j))
            if char != ".":
                obs[char] |= {(i, j)}


@cache
def obs_at(t, d=None):
    if not d:
        union = set()
        for dd in "<>":
            union |= obs_at(t % C, dd)
        for dd in "v^":
            union |= obs_at(t % R, dd)
        return union
    dy, dx = directions[d]
    return {((by + dy * t) % R, (bx + dx * t) % C) for by, bx in obs[d]}


def pathfind(init=(start, 0), dest=end):
    Q = [init]
    visited = set()
    while Q:
        pos, time = Q.pop(0)

        if pos == dest:
            return time

        if (pos, time) in visited:
            continue
        visited.add((pos, time))

        obs_time = obs_at(time + 1)
        if pos not in obs_time:
            Q.append((pos, time + 1))

        py, px = pos
        for dy, dx in directions.values():
            next_pos = (py + dy, px + dx)
            if next_pos not in valid:
                continue
            if next_pos in obs_time:
                continue
            Q.append((next_pos, time + 1))


def part_one():
    print(pathfind())


def part_two():
    print(pathfind((start, pathfind((end, pathfind()), start))))


part_one()
part_two()
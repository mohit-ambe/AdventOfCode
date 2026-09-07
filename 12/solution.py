file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

shapes = []
regions = []
reqs = []

row_iter = 0
for line in myin:
    if not line:
        continue
    elif line[0].isdigit() and line[1] == ":":
        shapes.append([])
    elif "." in line or "#" in line:
        shapes[-1] += [(row_iter, c) for c, char in enumerate(line) if char == "#"]
        row_iter += 1
    elif "x" in line:
        bounds, presents = line.split(": ")
        regions.append(tuple(map(int, bounds.split("x"))))
        presents = list(map(int, presents.split(" ")))
        reqs.append({p: count for p, count in enumerate(presents) if count})


def part_one():
    total = 0
    for region, req in zip(regions, reqs):
        # check if the solution is possible (optimal)
        # are there even enough spaces to hold the shapes?
        r, c = region
        volume = sum([len(shapes[i]) * req[i] for i in req])
        if volume > r * c:
            continue

        # check if the solution is possible (non-optimal)
        # are there enough 3x3 regions to house each shape independently?
        cubes = (r // 3) * (c // 3)
        if sum(req.values()) > cubes:
            continue

        total += 1

    print(total)


part_one()
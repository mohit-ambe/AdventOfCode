from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

coords = [tuple(map(int, line.split(","))) for line in myin]


def rectangle(x1, y1, x2, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def part_one():
    global coords
    area = 0

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            area = max(area, rectangle(*coords[i], *coords[j]))

    print(area)


def part_two():
    global coords
    points = coords.copy()

    points.sort(key=lambda p: (p[0], p[1]))
    x_edges = []
    for i in range(len(points) - 1):
        x1, y1, x2, y2 = *points[i], *points[i + 1]
        if x1 == x2:
            x_edges.append((x1, y1, y2))

    points.sort(key=lambda p: (p[1], p[0]))
    y_edges = []
    for i in range(len(points) - 1):
        x1, y1, x2, y2 = *points[i], *points[i + 1]
        if y1 == y2:
            y_edges.append((y1, x1, x2))

    @cache
    def inside(x, y):
        for xi, y1, y2 in x_edges:
            if min(y1, y2) <= y <= max(y1, y2) and xi == x:
                return True
        for yi, x1, x2 in y_edges:
            if min(x1, x2) <= x <= max(x1, x2) and yi == y:
                return True

        hits = 0
        for xi, y1, y2 in x_edges:
            if min(y1, y2) < y < max(y1, y2) and xi > x:
                hits += 1
        return hits % 2 == 1

    # to determine if a rectangle is valid,
    # sample every zth point
    z = 1480
    area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1, x2, y2 = *coords[i], *coords[j]

            region = rectangle(x1, y1, x2, y2)
            if region < area:
                continue

            if not (inside(x1, y2) and inside(x2, y1)):
                continue

            xa, xb = min(x1, x2), max(x1, x2)
            ya, yb = min(y1, y2), max(y1, y2)
            valid = True
            for x in range(xa, xb, z):
                for y in range(ya, yb, z):
                    valid = valid and inside(x, y)
                    if not valid:
                        break
                if not valid:
                    break
            if not valid:
                continue

            area = region
    print(area)


part_one()
part_two()

import ast

file = open("input.txt", "r")
myin = [line for line in file.readlines()]
file.close()

SAMPLE_INPUT = False

tiles = dict()
walls = dict()
start = tuple()
R, C = 0, 0
GS = 4 if SAMPLE_INPUT else 50

# transform = (dir, face) : (dir, face, (flip_y, flip_x, swap))
if SAMPLE_INPUT:
    top_lefts = [(0, 2), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)]
    T = open("transform_sample.txt", "r")
    transform = ast.literal_eval(T.read())
    T.close()
else:
    top_lefts = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (3, 0)]
    T = open("transform_input.txt", "r")
    transform = ast.literal_eval(T.read())
    T.close()

for i, line in enumerate(myin[:-2]):
    for j, char in enumerate(line):
        R, C = max(R, i + 1), max(C, j + 1)
        if not tiles:
            start = (i, j)
        for k, (tly, tlx) in enumerate(top_lefts):
            if tly * GS <= i < (tly + 1) * GS and tlx * GS <= j < (tlx + 1) * GS:
                if char == ".":
                    tiles[(i, j)] = k + 1
                if char == "#":
                    walls[(i, j)] = k + 1
                break

instructions = myin[-1].replace("R", ",R,").replace("L", ",L,").split(",")
instructions = list(map(lambda x: int(x) if x.isdigit() else x, instructions))

facing = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_one():
    y, x, f = *start, 0
    for d in instructions:
        if d == "L":
            f = (f - 1) % len(facing)
        elif d == "R":
            f = (f + 1) % len(facing)
        else:
            for _ in range(d):
                dy, dx = facing[f]
                next_tile = (y + dy, x + dx)
                if next_tile in walls:
                    break

                if next_tile not in tiles:
                    ny, nx = (y + dy) % R, (x + dx) % C
                    while (ny, nx) not in tiles and (ny, nx) not in walls:
                        ny, nx = (ny + dy) % R, (nx + dx) % C
                    next_tile = (ny, nx)

                if next_tile in walls:
                    break
                else:
                    y, x = next_tile
    print(1000 * (y + 1) + 4 * (x + 1) + f)


def part_two():
    y, x = start
    f = facing[0]
    surface_index = 1
    for d in instructions:
        if d == "L":
            fi = facing.index(f)
            f = facing[(fi - 1) % len(facing)]
        elif d == "R":
            fi = facing.index(f)
            f = facing[(fi + 1) % len(facing)]
        else:
            nf, ns = f, surface_index
            for _ in range(d):
                dy, dx = f
                next_tile = (y + dy, x + dx)
                if next_tile in walls:
                    break

                ny, nx = next_tile
                nf, ns = f, surface_index

                if (ny, nx) not in walls and tiles.get((ny, nx), -1) != surface_index:
                    tly, tlx = top_lefts[surface_index - 1]
                    # reshape into offsets from top left of the current cube face
                    ny = y - tly * GS
                    nx = x - tlx * GS

                    # transform
                    nf, ns, (fy, fx, tp) = transform[(f, surface_index)]
                    if fy:
                        ny = GS - 1 - ny
                    if fx:
                        nx = GS - 1 - nx
                    if tp:
                        ny, nx = nx, ny

                    # reshape back into flat coords
                    tly, tlx = top_lefts[ns - 1]
                    ny = ny + tly * GS
                    nx = nx + tlx * GS

                next_tile = (ny, nx)
                if next_tile in walls:
                    break
                else:
                    y, x = next_tile
                    f = nf
                    surface_index = ns
    print(1000 * (y + 1) + 4 * (x + 1) + facing.index(f))


part_one()
part_two()
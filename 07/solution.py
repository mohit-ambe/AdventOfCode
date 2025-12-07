from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

grid = [[*line] for line in myin]
start = 0, grid[0].index("S")


def part_one():
    splits = set()

    @cache
    def beam(y, x):
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            return 0
        if grid[y][x] == "^":
            splits.add((y, x))
            beam(y, x - 1)
            beam(y, x + 1)
        else:
            beam(y + 1, x)

    beam(*start)
    print(len(splits))


def part_two():
    @cache
    def beam(y, x):
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            return 0
        if y == len(grid) - 1:
            return 1
        if grid[y][x] == "^":
            return beam(y, x - 1) + beam(y, x + 1)
        else:
            return beam(y + 1, x)

    print(beam(*start))


part_one()
part_two()

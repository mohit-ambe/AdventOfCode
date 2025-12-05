file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

ranges = [list(map(int, line.split("-"))) for line in myin[:myin.index("")]]
nums = list(map(int, myin[myin.index("") + 1:]))


def part_one():
    fresh = 0
    for ingredient in nums:
        for a, b in ranges:
            if a <= ingredient <= b:
                fresh += 1
                break

    print(fresh)


def part_two():
    ranges.sort()

    change = True
    while change:
        change = False
        i = 0
        while i < len(ranges):
            a, b = ranges[i]
            j = i + 1
            while j < len(ranges):
                c, d = ranges[j]
                if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
                    a, b = min([a, b, c, d]), max([a, b, c, d])
                    ranges[i] = [a, b]
                    ranges.pop(j)
                    change = True
                    break
                j += 1
            i += 1

    print(sum([b - a + 1 for a, b in ranges]))


part_one()
part_two()

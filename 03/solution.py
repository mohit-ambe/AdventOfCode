file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def get_best_battery(bank, depth):
    joltage = 0
    left = 0
    for depth in range(depth, 0, -1):
        max = 0
        idx = left
        for i in range(left, len(bank) - depth + 1):
            x = int(bank[i])
            if x > max:
                idx, max = i, x
        left = idx + 1
        joltage = joltage * 10 + max
    return joltage


def part_one():
    print(sum([get_best_battery(bank, depth=2) for bank in myin]))


def part_two():
    print(sum([get_best_battery(bank, depth=12) for bank in myin]))


part_one()
part_two()

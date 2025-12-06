file = open("input.txt", "r")
myin = [line.replace("\n", "") for line in file.readlines()]
file.close()


def part_one():
    nums = [list(map(int, line.split())) for line in myin[:-1]]
    nums = list(zip(*nums))
    ops = myin[-1].split()

    total = 0
    for i, line in enumerate(nums):
        if ops[i] == "+":
            total += sum(line)
        else:
            t = 1
            for l in line:
                t *= l
            total += t
    print(total)


def part_two():
    ops = myin[-1].split()
    i = max([len(l) - 1 for l in myin[:-1]])

    total = 0

    for op in ops[::-1]:
        t = 1 if op == "*" else 0
        while i >= 0:
            num = "".join(["" if i >= len(line) else line[i] for line in myin[:-1]])
            i -= 1
            if num.isspace():
                break
            t = t + int(num) if op == "+" else t * int(num)
        total += t
    print(total)


part_one()
part_two()

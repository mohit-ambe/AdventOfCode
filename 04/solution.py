file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def both_parts():
    S = set()
    for r, line in enumerate(myin):
        for c, char in enumerate(line):
            if char == "@":
                S.add((r, c))
    original = len(S)

    remove = set()
    p1 = False
    while remove != set() or p1 is False:
        S = S - remove
        remove = set()
        for s in S:
            y, x = s
            count = len([s for dy, dx in directions if (y + dy, x + dx) in S])
            if count < 4:
                remove.add((y, x))
        if not p1:
            print(len(remove))
            p1 = True

    print(original - len(S))


both_parts()

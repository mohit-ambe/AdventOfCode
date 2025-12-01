file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def both_parts():
    dial = 50
    c1, c2 = 0, 0

    for num in myin:
        x = int(num[1:]) * (1 if num[0] == "R" else -1)
        dial += x
        if dial < 0 or dial > 99:
            c2 += abs(dial // 100)
        dial %= 100
        if dial == 0:
            c1 += 1

    print(c1)
    print(c2)


both_parts()

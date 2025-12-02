file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def both_parts():
    c1, c2 = 0, 0

    def is_repeating(word, segment, times):
        return segment * times == word

    for line in myin[0].split(","):
        a, b = list(map(int, line.split("-")))
        for i in range(a, b + 1):
            s = str(i)
            if is_repeating(s, s[:len(s) // 2], 2):
                c1 += i

            repeating = False
            for j in range(1, len(s)):
                if is_repeating(s, s[:j], len(s) // j):
                    repeating = True
                    break
            if repeating:
                c2 += i

    print(c1)
    print(c2)


both_parts()

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

elves = set()

for i, line in enumerate(myin):
    for j, char in enumerate(line):
        if char == "#":
            elves.add((i, j))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
checks = [
    [(-1, -1), (-1,  0), (-1,  1)],
    [( 1, -1), ( 1,  0), ( 1,  1)],
    [(-1, -1), ( 0, -1), ( 1, -1)],
    [(-1,  1), ( 0,  1), ( 1,  1)]
]

idx = 0
while True:
    candidates = dict()
    for ey, ex in elves:
        adj = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if (ey + dy, ex + dx) in elves:
                    adj += 1
        if adj == 1:
            candidates[(ey, ex)] = candidates.get((ey, ex), []) + [(ey, ex)]
            continue
        proposed = False
        for rotation in range(4):
            dy, dx = directions[(rotation + idx) % 4]
            valid = True
            for cy, cx in checks[(rotation + idx) % 4]:
                if (ey + cy, ex + cx) in elves:
                    valid = False
                    break
            if valid:
                candidates[(ey + dy, ex + dx)] = candidates.get((ey + dy, ex + dx), []) + [(ey, ex)]
                proposed = True
                break
        if not proposed:
            candidates[(ey, ex)] = candidates.get((ey, ex), []) + [(ey, ex)]
    new_elves = set()
    for candidate, origins in candidates.items():
        new_elves |= {candidate} if len(origins) == 1 else set(origins)
    if elves - new_elves == set():
        print(idx + 1)
        break
    elves = new_elves.copy()
    idx += 1
    if idx == 10:
        tl, br = list(elves)[:2]
        for ney, nex in new_elves:
            tl = min(tl[0], ney), min(tl[1], nex)
            br = max(br[0], ney), max(br[1], nex)

        print((br[0] - tl[0] + 1) * (br[1] - tl[1] + 1) - len(elves))
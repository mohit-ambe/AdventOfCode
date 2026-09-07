from sympy import Eq, solve, symbols

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

positions = []
velocities = []

for line in myin:
    pos, vel = line.split(" @ ")
    positions.append(list(map(int, pos.split(", "))))
    velocities.append(list(map(int, vel.split(", "))))


def part_one():
    LBOUND = 200_000_000_000_000
    UBOUND = 400_000_000_000_000
    valid = 0

    for i in range(len(myin)):
        for j in range(i + 1, len(myin)):
            px1, py1, pz1 = positions[i]
            vx1, vy1, vz1 = velocities[i]
            px2, py2, pz2 = positions[j]
            vx2, vy2, vz2 = velocities[j]

            if vy1 / vx1 == vy2 / vx2:
                continue

            stone1 = py1 - vy1 / vx1 * px1
            stone2 = py2 - vy2 / vx2 * px2

            x = (stone2 - stone1) / ((vy1 / vx1) - (vy2 / vx2))
            y = vy1 / vx1 * x + stone1
            t1 = (x - px1) / vx1
            t2 = (x - px2) / vx2

            if not LBOUND <= x <= UBOUND:
                continue
            if not LBOUND <= y <= UBOUND:
                continue
            if t1 < 0 or t2 < 0:
                continue

            valid += 1

    print(valid)


def part_two():
    pxr, pyr, pzr, vxr, vyr, vzr = symbols('pxr pyr pzr vxr vyr vzr', int=True)
    t_eqs = []

    for i in range(3):
        px, py, pz = positions[i]
        vx, vy, vz = velocities[i]
        t_eqs.append(Eq((pxr - px) * (vy - vyr), (pyr - py) * (vx - vxr)))
        t_eqs.append(Eq((pyr - py) * (vz - vzr), (pzr - pz) * (vy - vyr)))
        t_eqs.append(Eq((pxr - px) * (vz - vzr), (pzr - pz) * (vx - vxr)))

    solution = solve(t_eqs, (pxr, pyr, pzr, vxr, vyr, vzr), dict=True)[0]
    print(solution[pxr] + solution[pyr] + solution[pzr])


part_one()
part_two()
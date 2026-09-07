import pulp
from sympy import symbols

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

lightings = [int("".join(["1" if s == "#" else "0" for s in line.split(" ")[0][1:-1]])[::-1], base=2) for line in myin]
wirings = [[tuple(map(int, s[1:-1].split(","))) for s in line.split(" ")[1:-1]] for line in myin]
joltages = [tuple(map(int, line.split(" ")[-1][1:-1].split(","))) for line in myin]
lines = list(zip(lightings, wirings, joltages))


def part_one():
    presses = 0
    for l, w, _ in lines:
        w = [sum([2 ** x for x in action]) for action in w]
        Q = [(0, 0)]
        best = 1e10
        while Q:
            score, state = Q.pop(0)
            if state == l:
                presses += score
                Q.clear()
                continue
            if score > best:
                continue
            for action in w:
                Q.append((score + 1, state ^ action))
            Q = sorted(set(Q))
    print(presses)


def part_two():
    presses = 0
    V = max(wirings, key=len)
    variables = symbols("".join([f"x{i}," for i in range(len(V))]))

    for _, w, j in lines:
        matrix = [[0 for _ in range(len(j))] for _ in range(len(w))] + [list(j)]
        for r in range(len(w)):
            for c in range(len(w[r])):
                matrix[r][w[r][c]] = 1
        matrix = list(zip(*matrix))

        problem = pulp.LpProblem("", pulp.LpMinimize)

        # search for the minimum, positive, integer solution
        variables = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(len(variables))]
        problem += pulp.lpSum(variables)

        for row in matrix:
            coefficients = row[:-1]
            constant = row[-1]
            problem += pulp.lpSum(c * v for c, v in zip(coefficients, variables)) == constant

        problem.solve(pulp.PULP_CBC_CMD(msg=False))
        presses += int(pulp.value(problem.objective))

    print(presses)


part_one()
part_two()
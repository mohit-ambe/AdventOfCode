file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

lines = [line.split(": ") for line in myin]
tree = {a: b.split(" ") for a, b in lines}
tree_inverse = dict()
for t in tree:
    for ti in tree[t]:
        tree_inverse[ti] = tree_inverse.get(ti, []) + [t]

visited = dict()


def pathfind(node, root='svr'):
    if 'root' not in visited or visited['root'] != root:
        visited.clear()
        visited['root'] = root

    if node == root:
        return 1
    if node not in tree_inverse:
        return 0
    if node in visited:
        return visited[node]

    total = 0
    for neighbor in tree_inverse[node]:
        total += visited.get(neighbor, pathfind(neighbor, root=root))
    visited[node] = total

    return total


def part_one():
    print(pathfind("out", "you"))


def part_two():
    dac = pathfind("dac", "svr")
    fft = pathfind("fft", "svr")
    outdac = pathfind("out", "dac")
    outfft = pathfind("out", "fft")
    dacfft = pathfind("dac", "fft")
    fftdac = pathfind("fft", "dac")

    # one of these will be 0
    print(max(outdac * dacfft * fft, outfft * fftdac * dac))


part_one()
part_two()
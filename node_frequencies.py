import sys
import re
import gzip

gfa = gzip.open(sys.argv[1], 'r', encoding = 'ascii')

gfa_nodes = {}

for line in gfa:
    if line[0] != "S":
        continue
    match line.split():
        case ["S", name, *rest]:
            node = int(name)
            if node not in gfa_nodes:
                gfa_nodes[node] = 0

gfa.seek(0)

for line in gfa:
    if line[0] != "W":
        continue

    path = line.split()[6]

    nodes = {int(x) for x in re.split("[<>]", path[1:])}

    for node in nodes:
        gfa_nodes[node] = gfa_nodes[node] + 1
gfa.close()


for node in gfa_nodes:
    print(node, gfa_nodes[node][0])

import sys
import re
import gzip

gfa = gzip.open(sys.argv[1], 'r')

gfa_edges = {}

for line in gfa:
    edge = None
    match line.decode('ascii').split():
        case ["L", left, "+", right, "+"]:
            edge = ">" + left + ">" + right
        case ["L", left, "-", right, "+"]:
            edge = "<" + left + ">" + right
        case ["L", left, "+", right, "-"]:
            edge = ">" + left + "<" + right
        case ["L", left, "-", right, "-"]:
            edge = "<" + left + "<" + right
            # save first and last nucleotide for each node
    gfa_edges[edge] = 0


for line in gfa:
    line = line.decode('ascii')
    if line[0] != "W":
        continue

    path = line.split()[6]

    nodes = re.split("([<>])", path)[1:]

    edges = ["".join(nodes[i:i + 4]) for i in range(0, len(nodes), 2)][:-1]

    for edge in edges:
        gfa_edges[edge] = gfa_edges[edge] + 1
gfa.close()

for edge in gfa_edges:
    print(edge, gfa_edges[edge])

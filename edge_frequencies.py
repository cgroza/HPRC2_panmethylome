import sys
import re
import gzip

flip = {'>' : '<', '<' : '>'}

gfa = gzip.open(sys.argv[1], 'rt', encoding = 'ascii')

gfa_edges = {}

for line in gfa:
    edge = None
    match line.split():
        case ["L", left, "+", right, "+", *rest]:
            edge = ">" + left + ">" + right
        case ["L", left, "-", right, "+", *rest]:
            edge = "<" + left + ">" + right
        case ["L", left, "+", right, "-", *rest]:
            edge = ">" + left + "<" + right
        case ["L", left, "-", right, "-", *rest]:
            edge = "<" + left + "<" + right
    gfa_edges[edge] = 0

gfa.seek(0)

for line in gfa:
    if line[0] != "W":
        continue

    path = line.split()[6]

    nodes = re.split("([<>])", path)[1:]

    edges = [tuple(nodes[i:i + 4]) for i in range(0, len(nodes), 2)][:-1]

    for edge in edges:
        edge_str = "".join(edge)
        if edge_str in gfa_edges:
            gfa_edges[edge] = gfa_edges[edge] + 1
        # complement edge
        else:
            edge = (flip[edge[2]], edge[3], flip[edge[0]], edge[1])
            edge_str = "".join(edge)
            gfa_edges[edge] = gfa_edges[edge] + 1
gfa.close()

for edge in gfa_edges:
    print(edge, gfa_edges[edge])

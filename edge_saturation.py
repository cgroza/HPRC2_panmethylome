import sys
import re

gfa = open(sys.argv[1], 'r')

cpg = open(sys.argv[2], 'r')

cpgs = {}

for line in cpg:
    cpgs[line] = None
cpg.close()

current_hap = None
current_hap_i = 0

for line in gfa:
    if line[0] != "W":
        continue

    fields = line.split()
    hap = fields[1] + "#" + fields[2]
    path = fields[6]

    if(hap != current_hap):
        current_hap = hap
        current_hap_i += 1

    nodes = re.split("([<>])", path)[1:]

    edges = ["".join(nodes[i:i + 4]) for i in range(0, len(nodes), 2)][:-1]

    for edge in edges:
        if edge in cpgs and cpgs[edge] is None:
            cpgs[edge] = current_hap_i
gfa.close()


for edge in cpgs:
    print(edge, cpgs[edge])

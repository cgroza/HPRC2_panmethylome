import sys
import re

gfa = open(sys.argv[1], 'r')

cpg = open(sys.argv[2], 'r')

cpgs = {}

for line in cpg:
    node, offset, strand = line.split()
    node = int(node)
    if strand == "-":
        continue
    if node not in cpgs:
        cpgs[node] = (0, None)
    cpgs[node] = (cpgs[node][0] + 1, None)
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

    nodes = {int(x) for x in re.split("[<>]", path[1:])}

    for node in nodes:
        if node in cpgs and cpgs[node][1] is None:
            cpgs[node] = (cpgs[node][0], current_hap_i)
gfa.close()


for node in cpgs:
    print(node, cpgs[node][0], cpgs[node][1])

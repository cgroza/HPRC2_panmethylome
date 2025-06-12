import sys
import re
import gzip

gfa = gzip.open(sys.argv[1], 'rt', encoding = 'ascii')

cpg = open(sys.argv[2], 'r')

cpgs = {}


flip = {'>' : '<', '<' : '>'}

def complement(edge):
    return (flip[edge[2]], edge[3], flip[edge[0]], edge[1])

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

    edges = [tuple(nodes[i:i + 4]) for i in range(0, len(nodes), 2)][:-1]

    for edge in edges:
        if "".join(edge) in cpgs and cpgs[edge] is None:
            cpgs[edge] = current_hap_i
        # handle complement edge
        elif "".join(complement(edge)) in cpgs and cpgs["".join(complement(edge))] is None:
            cpgs["".join(complement(edge))] = current_hap_i
gfa.close()


for edge in cpgs:
    print(edge, cpgs[edge])

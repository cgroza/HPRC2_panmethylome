import sys

cpg_index = dict()

with open(sys.argv[1], 'r') as cpgs_file:
    for line in cpgs_file:
        node, offset, strand = line.rstrip().split(',')
        # no need to lift both nucleotides
        if strand == '-':
            continue
        if int(node) not in cpg_index:
            cpg_index[int(node)] = []
        cpg_index[int(node)].append((int(offset), strand))

gfa = open(sys.argv[2], 'r')

for line in gfa:
    if line[0] != "P":
        continue
    _, p_name, hap, _ = line.rstrip().split()
    hap_name = p_name

    if "CHM13" not in hap_name:
        continue

    hap_seq = hap.split(',')

    for node in hap_seq:
        node_name = int(node[:-1])
        strand = node[-1]

        if node_name in cpg_index:
            for cpg in cpg_index[node_name]:
                offset = cpg[0]
                # node lies reversed along assembly
                if strand == '-':
                    # 0 based coordinates, flip offset
                    offset = node_lengths[node_name] - offset - 1
                print(str(node_name) + ',' + str(cpg[0]) + ',' + cpg[1])

gfa.close()

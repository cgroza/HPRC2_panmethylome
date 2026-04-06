import sys

cpg_index = dict()

with open(sys.argv[1], 'r') as cpgs_file:
    for line in cpgs_file:
        node, offset, strand, cpgid = line.rstrip().split('\t')
        # no need to lift both nucleotides
        if strand == '-':
            continue
        if  ' ' in cpgid:
            continue
        if int(node) not in cpg_index:
            cpg_index[int(node)] = []
        cpg_index[int(node)].append(cpgid)

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
        if node_name in cpg_index:
            for cpg in cpg_index[node_name]:
                # node lies reversed along assembly
                print(cpg)

gfa.close()

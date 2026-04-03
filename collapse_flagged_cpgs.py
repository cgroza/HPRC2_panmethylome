import gzip
import sys
import BitVector

cpgs = gzip.open(sys.argv[1], 'rt')

with open(sys.argv[2], 'rt') as samples_file:
    i = 0
    sample_order = {}
    for line in samples_file:
        sample_order[line.rstrip()] = i
        i += 1


cpg_annot = dict()

def make_record():
    return BitVector.BitVector(size = 466)

for line in cpgs:
    cpg_contig, cpg_start, cpg_end, cpg_id = line.rstrip().split('\t')

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    genome = cpg_contig.split("#")[:2]
    if genome[0].startswith("CHM13") or genome[0].startswith("GRCh38"):
        genome = genome[:1]

    sample = "#".join(genome)

    cpg_annot[cpg_id][sample_order[sample]] = 1

for cpg_id in cpg_annot:
    print(cpg_id, cpg_annot[cpg_id].count_bits(), sep = '\t')

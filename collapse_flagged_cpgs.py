import gzip
import sys

cpgs = gzip.open(sys.argv[1], 'rt')

cpg_annot = dict()

def make_record():
    return set()

for line in cpgs:
    cpg_contig, cpg_start, cpg_end, cpg_id = line.rstrip().split('\t')

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    genome = cpg_contig.split("#")[:2]
    if genome.startswith("CHM13") or genome.startwith("GRCh38"):
        genome = genome[0]

    cpg_annot[cpg_id].add("#".join(genome))

for cpg_id in cpg_annot:
    print(cpg_id, len(cpg_annot[cpg_id]), sep = '\t')

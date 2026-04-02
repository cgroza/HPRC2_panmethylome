import gzip
import sys
import rbloom

cpgs = gzip.open(sys.argv[1], 'rt')


cpg_annot = dict()

bf = rbloom.Bloom(int(464 * 53e6), 0.1)

def make_record():
    return 0

for line in cpgs:
    cpg_contig, cpg_start, cpg_end, cpg_id = line.rstrip().split('\t')

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    genome = cpg_contig.split("#")[:2]
    if genome[0].startswith("CHM13") or genome[0].startswith("GRCh38"):
        genome = genome[:1]

    bf_id = "#".join(genome) + "," + cpg_id

    if bf_id not in bf:
        cpg_annot[cpg_id] = cpg_annot[cpg_id] + 1
        bf.add(bf_id)

for cpg_id in cpg_annot:
    print(cpg_id, cpg_annot[cpg_id], sep = '\t')

import gzip
import sys

promoters = gzip.open(sys.argv[1], 'rt')

cpg_annot = dict()

def make_record():
    return 0

for line in segdups:
    cpg_contig, cpg_start, cpg_end, cpg_id, asm_contig, asm_start, asm_end = line.rstrip().split('\t')

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    if asm_contig == '.':
        continue

    # cpg_annot[cpg_id].add(asm_contig + ':' + asm_start + '-' + asm_end + ':' + sv_type)
    cpg_annot[cpg_id] += 1

for cpg_id in cpg_annot:
    print(cpg_id, cpg_annot[cpg_id], sep = '\t')

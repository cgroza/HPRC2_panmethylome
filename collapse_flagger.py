import gzip
import sys

flagger = gzip.open(sys.argv[1], 'rt')

cpg_annot = dict()

def make_record():
    return set()

for line in flagger:
    cpg_contig, cpg_start, cpg_end, cpg_id, asm_contig, asm_start, asm_end, err_type, _, _, err_start, err_end, rgb = line.rstrip().split('\t')

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    if asm_contig == '.':
        continue

    cpg_annot[cpg_id].add("#".join(asm_contig.split("#")[:2]))

for cpg_id in cpg_annot:
    print(cpg_id, len(cpg_annot[cpg_id]), sep = '\t')

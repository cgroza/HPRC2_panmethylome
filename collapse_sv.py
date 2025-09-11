import gzip
import sys

sv = gzip.open(sys.argv[1], 'rt')

cpg_annot = dict()

def make_record():
    return set()

for line in sv:
    cpg_contig, cpg_start, cpg_end, cpg_id, asm_contig, asm_start, asm_end, sv_id, sv_type = line.rstrip().split('\t')

    if asm_contig == '.':
        continue

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    # cpg_annot[cpg_id].add(asm_contig + ':' + asm_start + '-' + asm_end + ':' + sv_type)
    cpg_annot[cpg_id].add(sv_type)

for cpg_id in cpg_annot:
    print(cpg_id, ";".join(cpg_annot[cpg_id]), sep = '\t')

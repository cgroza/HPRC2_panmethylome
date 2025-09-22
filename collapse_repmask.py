import gzip
import sys

repmask = gzip.open(sys.argv[1], 'rt')

cpg_annot = dict()

def make_record():
    return set()

for line in repmask:
    cpg_contig, cpg_start, cpg_end, cpg_id, asm_contig, asm_start, asm_end, rep_id, rep_fam = line.rstrip().split('\t')


    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    if asm_contig == '.':
        continue

    # cpg_annot[cpg_id].add(asm_contig + ':' + asm_start + '-' + asm_end + ':' + sv_type)
    cpg_annot[cpg_id].add(rep_fam)

for cpg_id in cpg_annot:
    print(cpg_id, ";".join(sorted(cpg_annot[cpg_id])), sep = '\t')

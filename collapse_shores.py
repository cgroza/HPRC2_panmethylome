import gzip
import sys
import re

shores = gzip.open(sys.argv[1], 'rt')

cpg_annot = dict()

def make_record():
    return set()

for line in shores:
    cpg_conting, cpg_start, cpg_end, cpg_id, asm, asm_start, asm_end = line.split('\t')

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    if asm_start == '.':
        continue

    cpg_annot[cpg_id].add("T")

for cpg_id in cpg_annot:
    print(cpg_id, ";".join(cpg_annot[cpg_id]), sep = '\t')

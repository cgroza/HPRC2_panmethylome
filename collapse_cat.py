import gzip
import sys
import re

cat = gzip.open(sys.argv[1], 'rt')

gene_regex = re.compile(r'(gene_name|gene)=([^;]+)')

cpg_annot = dict()

def make_record():
    return set()

for line in cat:
    cpg_conting, cpg_start, cpg_end, cpg_id, _, annot, feature , _, _, _, _, _, desc = line.split('\t')

    if cpg_id not in cpg_annot:
        cpg_annot[cpg_id] = make_record()

    if annot == '.':
        continue

    gene = '.'
    try:
        gene = gene_regex.search(desc).group(2)
    except:
        pass


    cpg_annot[cpg_id].add(feature + ':' + gene)

for cpg_id in cpg_annot:
    print(cpg_id, ";".join(cpg_annot[cpg_id]), sep = '\t')

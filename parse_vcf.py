import sys

for line in sys.stdin:
    chrom, pos, svlen, svid, tig, svtype, gt, name = line.split()

    if tig == '.':
        continue

    p1, p2 = gt.split('|')

    phases = []
    if p1 == "1":
        phases.append('1')
    if p2 == "1":
        phases.append('2')

    assert len(phases) == len(tig.split(','))

    for svid, tig, phase in zip(svid.split(';'), tig.split(','), phases):
        contig = tig.split(':')[0]
        start, end = tig.split(':')[1].split('-')

        if svtype == 'DEL':
            pos = int(pos)
            svlen = int(svlen)
            print('CHM13#' + chrom, pos, pos + abs(svlen), svid, svtype, sep = '\t')
        if '#' in tig:
            print(contig, start, end, svid, svtype, sep = '\t')
        else:
            print(name + '#' + phase + '#' + contig, start, end, svid, svtype, sep = '\t')

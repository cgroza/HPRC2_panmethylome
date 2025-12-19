import intervaltree
import sys
import gzip

segdups = open(sys.argv[1], 'r')
flagger = gzip.open(sys.argv[2], 'rt', encoding='ascii')

intervals = dict()

flagger.readline()
for line in flagger:
    contig, start, end, *rest = line.split('\t')
    if contig not in intervals:
        intervals[contig] = intervaltree.IntervalTree()
    intervals[contig][int(start): int(end)] = 1
flagger.close()

header = segdups.readline().split('\t')
sys.stdout.write('\t'.join(header))

for line in segdups:
    fields = dict(zip(header, line.split('\t')))

    prune = False

    if fields['#chr1'] in intervals:
        if intervals[fields['#chr1']][int(fields['start1']) : int(fields['end1'])]:
            prune = True

    if fields['chr2'] in intervals:
        if intervals[fields['chr2']][int(fields['start2']) : int(fields['end2'])]:
            prune = True

    if not prune:
        sys.stdout.write(line)

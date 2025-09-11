import sys

header = sys.stdin.readline()[1:].split()

for line in sys.stdin:
    if line[0] == '#':
        header = line[1:].split()
        continue
    segdup = dict(zip(header, line.split()))
    print(segdup['chr1'], segdup['start1'], segdup['end1'], segdup['name'], sep = '\t')
    print(segdup['chr2'], segdup['start2'], segdup['end2'], segdup['name'], sep = '\t')

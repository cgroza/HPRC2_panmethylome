import sys

while True:
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    if not (line1 and line2):
        continue

    node1, offset1, strand1, depth1, score1, cpg_id1 = line1.rstrip().split('\t')
    node2, offset2, strand2, depth2, score2, cpg_id2 = line2.rstrip().split('\t')

    assert cpg_id1 == cpg_id2

    print(node1, offset1, strand1,
          int(depth1) + int(depth2),
          (float(score1) * int(depth1) + float(score2) * int(depth2))/(int(depth1) + int(depth2)),
          cpg_id1, sep = '\t')


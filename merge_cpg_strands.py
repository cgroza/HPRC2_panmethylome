import sys

print(sys.stdin.readline().rstrip())
while True:
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    if not (line1 and line2):
        break

    node1, offset1, strand1, depth1, score1, cpg_id1 = line1.rstrip().split('\t')
    node2, offset2, strand2, depth2, score2, cpg_id2 = line2.rstrip().split('\t')

    assert cpg_id1 == cpg_id2

    if float(depth1) + float(depth2) < 1:
        print(node1, offset1, strand1,
            "0", "0",
            cpg_id1, sep = '\t')
        continue

    print(node1, offset1, strand1,
          float(depth1) + float(depth2),
          (float(score1) * float(depth1) + float(score2) * float(depth2))/(float(depth1) + float(depth2)),
          cpg_id1, sep = '\t')


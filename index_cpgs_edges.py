import sys

gfa = open(sys.argv[1])

node_ends = {}

for line in gfa:
    match line.split():
        case ["S", name, seq, *rest]:
            # save first and last nucleotide for each node
            node_ends[name] = (seq[0], seq[-1])

gfa.seek(0)

for line in gfa:
    match line.split():
        case ["L", left, "+", right, "+", *rest]:
            if node_ends[left][1] + node_ends[right][0] == "CG":
                print(">" + left, ">" + right)
        case ["L", left, "+", right, "-", *rest]:
            if node_ends[left][1] + node_ends[right][1] == "CC":
                print(">" + left, "<" + right)
        case ["L", left, "-", right, "+", *rest]:
            if node_ends[left][0] + node_ends[right][0] == "GG":
                print("<" + left, ">" + right)
        case ["L", left, "-", right, "-", *rest]:
            if node_ends[left][0] + node_ends[right][1] == "GC":
                print("<" + left, "<" + right)

gfa.close()

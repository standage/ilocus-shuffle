import sys
prevgene = None
print('Length\tGene1\tGene2')
for line in sys.stdin:
    fields = line.rstrip().split()
    if len(fields) != 9 or fields[2] != 'gene':
        continue
    if prevgene is None or fields[0] != prevgene[0]:
        prevgene = fields
        continue

    #print('DEBUG line="%s" pregene="%s"' % (line, prevgene))
    start = int(fields[3])
    prev_end = int(prevgene[4])
    #print('DEBUG start=%s prev_end=%s' % (fields[3], prevgene[4]))
    distance = start - prev_end - 1
    print(distance, prevgene[8], fields[8], sep='\t')
    prevgene = line
#!/usr/bin/env python

from __future__ import print_function
import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('gff3', type=argparse.FileType('r'))
args = parser.parse_args()

both, neither, rightonly, leftonly = 0, 0, 0, 0
for line in args.gff3:
    if '\tlocus\t' not in line or 'child_gene=' not in line:
        continue
    liil = None
    lmatch = re.search('liil=(\d+)', line)
    if lmatch:
        liil = int(lmatch.group(1))
    riil = None
    rmatch = re.search('riil=(\d+)', line)
    if rmatch:
        riil = int(rmatch.group(1))
    print(liil, riil, sep='\t', file=sys.stderr)

    if liil and riil:
        both += 1
    elif liil:
        leftonly += 1
    elif riil:
        rightonly += 1
    else:
        neither += 1

print('left&right=%d' % both)
print('leftonly=%d' % leftonly)
print('rightonly=%d' % rightonly)
print('neither=%d' % neither)
print('total=%d' % (both + leftonly + rightonly + neither))

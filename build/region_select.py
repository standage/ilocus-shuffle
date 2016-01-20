#!/usr/bin/env python
#
# Copyright (c) 2015   Daniel Standage <daniel.standage@gmail.com>
# Copyright (c) 2015   Indiana University
# All rights reserved.
#
# This file is released under the BSD 3-clause license.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

from __future__ import print_function
import argparse
import random
import re
import subprocess
import sys


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, default=1000000,
                        help='size of fragment(s) to extract; default is '
                        '1000000 (1 Mb)')
    parser.add_argument('--numfrags', type=int, default=10,
                        help='number of fragments to extract; default is 10')
    parser.add_argument('--seed', type=int, help='random seed')
    parser.add_argument('--out', type=argparse.FileType('w'),
                        default=sys.stdout, help='output file')
    parser.add_argument('locusgff3', type=argparse.FileType('r'))
    parser.add_argument('genegff3')
    return parser


def store_seq(seqs, line, size=1000000):
    match = re.search('##sequence-region\s+(\S+)\s+(\d+)\s+(\d+)', line)
    assert match, 'unable to parse sequence region pragma: ' + line
    assert match.group(2) == '1'
    seqdata = (match.group(1), int(match.group(2)), int(match.group(3)))
    if seqdata[2] < size:
        return
    seqs.append(seqdata)


def seq_dict(seqs, size=1000000, maxseqs=10):
    regions = dict()
    random.shuffle(seqs)
    for seqid, seqstart, seqend in seqs[:maxseqs]:
        maxindex = seqend - size + 1
        start = random.randint(1, maxindex)
        end = start + size - 1
        regions[seqid] = (start, end)
    return regions


def sample_regions(gff3, size, maxseqs):
    seqs = list()
    regions = dict()
    starts = dict()
    ends = dict()
    for line in gff3:
        if line.startswith('##sequence-region'):
            store_seq(seqs, line, size=size)
        elif '\tlocus\t' in line:
            if len(regions) == 0:
                regions = seq_dict(seqs, size=size, maxseqs=maxseqs)
            fields = line.rstrip().split('\t')
            assert len(fields) == 9
            seqid = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            if seqid not in regions:
                continue
            regiondata = regions[seqid]
            if start <= regiondata[1] and end >= regiondata[0]:  # overlap?
                if seqid not in starts or start < starts[seqid]:
                    starts[seqid] = start
                if seqid not in ends or end > ends[seqid]:
                    ends[seqid] = end

    for seqid in sorted(regions):
        yield seqid, starts[seqid], ends[seqid]


def main():
    args = parser().parse_args()
    if not args.seed:
        args.seed = random.randint(0, sys.maxsize)
    random.seed(args.seed)
    print('Random seed: %d' % args.seed, file=sys.stderr)

    agg_cmd = ['gt', 'gff3', '-sort', '-tidy']
    rm_cmd = ['rm']
    for seqid, start, end in sample_regions(args.locusgff3, args.size,
                                            args.numfrags):
        # print('DEBUG start=%r end=%r' % (type(start), type(end)), file=sys.stderr)
        select_proc = subprocess.Popen(['gt', 'select', '-seqid', seqid,
                                        '-contain', str(start), str(end),
                                        args.genegff3],
                                       stdout=subprocess.PIPE,
                                       universal_newlines=True)
        gff3_proc = subprocess.Popen(['gt', 'gff3', '-sort', '-tidy',
                                      '-offset', '-%d' % (start - 1), '-o',
                                      seqid + '.temp.gff3', '-force'],
                                     stdin=select_proc.stdout,
                                     universal_newlines=True)
        gff3_proc.communicate()
        agg_cmd.append('%s.temp.gff3' % seqid)
        rm_cmd.append('%s.temp.gff3' % seqid)
    subprocess.check_call(agg_cmd, stdout=args.out)
    subprocess.check_call(rm_cmd)


if __name__ == '__main__':
    main()

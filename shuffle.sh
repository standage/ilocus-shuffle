#!/usr/bin/env bash
set -eo pipefail

WD=$1
species=$2

prefix=${WD}/${species}/${species}
shufdir=${WD}/${species}/shuffled
shprefix=${shufdir}/${species}
mkdir -p $shufdir

# Randomly select six 1 Mb regions from the genome
./region_select.py --seed=54321 --size=1000000 --numfrags=6 --out=${shprefix}.orig.gff3 ${prefix}.iloci.gff3 ${prefix}.gff3
# Compute iLoci
locuspocus --delta=500 --verbose --skipends --outfile=${shprefix}.orig.iloci.gff3 --ilens=${shprefix}.orig.ilens.tsv ${shprefix}.orig.gff3
miloci.py < ${shprefix}.orig.iloci.gff3 > ${shprefix}.orig.miloci.gff3
# Shuffle the iLocus features
./shuffle_iloci.py --seed=54321 --out=${shprefix}.shuffled.gff3 ${shprefix}.orig.iloci.gff3
# Recompute iLoci on the shuffled features
locuspocus --delta=500 --verbose --skipends --outfile=${shprefix}.shuffled.iloci.gff3 --ilens=${shprefix}.shuffled.ilens.tsv ${shprefix}.shuffled.gff3
miloci.py < ${shprefix}.shuffled.iloci.gff3 > ${shprefix}.shuffled.miloci.gff3
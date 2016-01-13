#!/usr/bin/env bash
set -eo pipefail

species=$1
prefix=species/${species}/shuffled/${species}

echo ""
echo ""
echo "===== $species ====="

echo ""
echo "As annotated"
echo "------------"
./filens.py ${prefix}.orig.iloci.gff3 > ${prefix}.orig.filens.tsv
echo ""
echo "Shuffled"
echo "--------"
./filens.py ${prefix}.shuffled.iloci.gff3 > ${prefix}.shuffled.filens.tsv
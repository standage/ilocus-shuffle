#!/usr/bin/env bash
set -eo pipefail

species=$1
prefix=../species/${species}/shuffled/${species}

orig()
{
    echo ""
    echo "As annotated"
    echo "------------"
    ./filens.py ${prefix}.orig.iloci.gff3 2> ${prefix}.orig.filens.tsv
}

shuffled()
{
    echo ""
    echo "Random"
    echo "------"
    ./filens.py ${prefix}.shuffled.iloci.gff3 2> ${prefix}.shuffled.filens.tsv
}

echo ""
echo ""
echo "===== $species ====="

paste <(orig) <(shuffled)

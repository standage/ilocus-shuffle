#!/usr/bin/env bash
set -eo pipefail

species=$1
prefix=../species/${species}/shuffled/${species}

percentage()
{
    local locusfile=$1
    ziloci=$(grep -c -w 0 $locusfile || true)
    total=$(grep -c -w . $locusfile || true)
    perc=$(awk "BEGIN { print $ziloci / $total * 100 }")
    printf "\t%d/%d=%.1lf%%" $ziloci $total $perc
}

printf $species
percentage ${prefix}.orig.ilens.tsv
percentage ${prefix}.shuffled.ilens.tsv
echo ""

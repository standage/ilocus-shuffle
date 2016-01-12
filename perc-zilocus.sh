#!/usr/bin/env bash
set -eo pipefail

species=$1
prefix=species/${species}/shuffled/${species}

percentage()
{
    local locusfile=$1
    ziloci=$(grep -c -w 0 $locusfile)
    total=$(grep -c -w . $locusfile)
    perc=$(awk "BEGIN { print $ziloci / $total }")
    echo "$locusfile $ziloci / $total = $perc"
}

percentage ${prefix}.orig.ilens.tsv
percentage ${prefix}.shuffled.ilens.tsv
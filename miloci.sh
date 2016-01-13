#!/usr/bin/env bash
set -eo pipefail

milocus_breakdown()
{
    local milocusfile=$1
    perl -ne 'm/child_gene=(\d+)/ and print "$1\n"' \
            < $milocusfile \
        | sort -n \
        | uniq -c \
        | tail -n +2
}

species=$1
prefix=species/${species}/shuffled/${species}

echo ""
echo $species

milocus_breakdown ${prefix}.orig.miloci.gff3
milocus_breakdown ${prefix}.shuffled.miloci.gff3

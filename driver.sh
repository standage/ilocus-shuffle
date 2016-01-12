#!/usr/bin/env bash
set -eo pipefail

WD=species
# pip install genhub
# genhub-build.py --workdir=$WD --conf=Atha,Cele,Dmel,Drer,Scer --numprocs=4 download format prepare stats
parallel --gnu --jobs=5 bash shuffle.sh species {} ::: Amel Bter Hsal Cflo Pdom Nvit # Osat # Atha Cele Dmel Drer Scer

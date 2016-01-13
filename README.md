# iLocus Shuffling

```
# hym: Amel, Bter, Hsal, Cflo, Pdom, Nvit
# plant: Atha, Bdis, Osat
genhub-build.py --numprocs=4 --workdir=scratch/species/ --cfgdir=scratch/tempconf prepare stats

#
parallel --gnu --jobs=4 bash shuffle.sh species {} ::: Amel Bter Hsal Cflo Pdom Nvit Atha Bdis Osat
```

## Shuffling iLoci results in fewer ziLoci by a substantial margin.

```
for species in Amel Bter Hsal Cflo Pdom Nvit Atha Bdis Osat; do
    ./perc-zilocus.sh $species
done
```

## Shuffling iLoci results in fewer miLoci, shorter miLoci, and fewer genes per miLocus.

```
for species in Amel Bter Hsal Cflo Pdom Nvit Atha Bdis Osat; do
    ./miloci.sh $species
done
```

See also `miLocusCountLength.ipynb`.

## Shuffling iLoci results increase the number of giLoci flanked on one or both sides by iiLoci

```
for species in Amel Bter Hsal Cflo Pdom Nvit Atha Bdis Osat; do
    ./filens-drive.sh $species
done
```
# iLocus Shuffling

```
# insect: Amel, Bter, Hsal, Cflo, Pdom, Nvit, Dmel
# plant: Atha, Bdis, Osat
# vertebrate: Xtro (Xenopus tropicalis), Drer (Danio rerio), Btau (Bos taurus), Mmus (Mus musculus)
specieslist="Amel Bter Hsal Cflo Pdom Nvit Dmel Atha Bdis Osat Xtro Drer Btau Mmus"
```

## Shuffling iLoci results in fewer ziLoci by a substantial margin.

```
for species in $specieslist; do
    ./perc-zilocus.sh $species
done
```

See `iiLoci.ipynb` and `adjacent-iiLoci.ipynb`.
The trend is much more drastic for insects than for plants, and it's only a slight increase in vertebrates.

## Shuffling iLoci results in fewer miLoci, shorter miLoci, and fewer genes per miLocus.

```
for species in ; do
    ./miloci.sh $species
done
```

See also `miLocusCountLength.ipynb`.

## Shuffling iLoci increases the number of giLoci flanked on one or both sides by iiLoci

```
for species in Amel Bter Hsal Cflo Pdom Nvit Atha Bdis Osat; do
    ./filens-drive.sh $species
done
```

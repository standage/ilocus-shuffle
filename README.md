# iLocus Shuffling

## Species studied

- insects: Amel, Bter, Hsal, Cflo, Pdom, Nvit, Dmel
- plants: Atha, Bdis, Osat
- vertebrates: Xtro (Xenopus tropicalis), Drer (Danio rerio), Btau (Bos taurus), Mmus (Mus musculus)

## iLocus shuffling procedure

*iLocus shuffling* would be more accurately described as *random distribution of giLoci*.
The procedure, on a per-sequence basis, is this.

- select the gene-containing iLoci (giLoci) for the sequence
- shuffle the giLoci
- re-distribute the giLoci (and attached gene features) on the sequence randomly, such that giLoci don't overlap
- re-compute iLocus boundaries and neighbor statistics on re-distributed genes

Six sequences > 1Mb in length were selected from each species, and a 1Mb region was sampled randomly from each.
All of the statistics and results reported here were done on this subset of data.
The selection is reproducible with the given random seed(s).

## Results

- [Shuffling iLoci results in fewer ziLoci by a substantial margin](ziloci/)
- [Shuffling iLoci results in fewer miLoci, shorter miLoci, and fewer genes per miLocus](miloci/)
- [Shuffling iLoci decreases the number of giLoci flanked on one or both sides by ziLoci](filens/)

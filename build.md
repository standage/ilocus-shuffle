```
genhub-build.py --numprocs=4 --workdir=scratch/species/ --cfgdir=scratch/tempconf download format prepare stats
parallel --gnu --jobs=4 bash shuffle.sh species {} ::: Amel Bter Hsal Cflo Pdom Nvit Dmel Atha Bdis Osat Xtro Drer Btau Mmus
```

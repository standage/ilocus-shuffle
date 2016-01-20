# iiLoci and ziLoci

## Terminology refresher

- iiLocus: intergenic locus, flanked on both sides by giLoci (gene-containing iLoci)
- ziLocus: zero-length iLocus, two genes so close together that their corresponding iLoci abut or overlap, where otherwise an iiLocus would have been

## Results

The occurrence of ziLoci is dramatically reduced with randomly distributed iLoci.

The following shows, by species, the number and proportion of iiLoci that are zero-length before and after shuffling.
```
$ make
Species	AsAnnotated	Random
Amel	91/192=47.4%	21/192=10.9%
Bter	136/248=54.8%	38/248=15.3%
Hsal	119/215=55.3%	22/215=10.2%
Cflo	135/261=51.7%	41/261=15.7%
Pdom	189/360=52.5%	17/360=4.7%
Nvit	179/307=58.3%	38/307=12.4%
Dmel	359/539=66.6%	117/539=21.7%
Atha	747/1182=63.2%	696/1182=58.9%
Bdis	136/404=33.7%	29/404=7.2%
Osat	111/449=24.7%	22/449=4.9%
Xtro	18/121=14.9%	8/121=6.6%
Drer	18/103=17.5%	4/103=3.9%
Btau	6/68=8.8%	0/68=0.0%
Mmus	38/141=27.0%	6/141=4.3%
```

The [`iiLoci.ipynb`](iiLoci.ipynb) notebook has plots of the length distribution of iiLoci (without ziLoci) for each species, and [`adjacent-iiLoci.ipynb`](adjacent-iiLoci.ipynb) shows plots of the distribution of aggregate lengths of 3 adjacent iiLoci (ziLoci included).
The shuffling does have an effect to some extent on these length distributions, but the most drastic and consistent effect is the reduction in ziLoci.

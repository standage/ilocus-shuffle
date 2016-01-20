specieslist="Amel Bter Hsal Cflo Pdom Nvit Dmel Atha Bdis Osat Xtro Drer Btau Mmus"
all:
	@ echo "Two pairs of columns:"
	@ echo "    first pair = iLoci as annotated, second pair = randomly distributed"
	@ echo "    first value = frequency, second value = genes per miLocus"
	@ for species in "$(specieslist)"; do ./miloci.sh $$species; done

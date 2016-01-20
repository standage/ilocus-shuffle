# miLoci

## Terminology refresher

- miLocus: merged iLocus, formed by joining two or more giLoci that abut or overlap due to the proximity of their resident genes

## Results

On average, random distribution of iLoci results in fewer miLoci, shorter miLoci, and fewer genes per miLocus.
The [miloci.ipynb](miloci.ipynb) notebook shows plots of miLocus length distributions for each species, and the distributions of gene counts per locus are shown below.

```
$ make
Two pairs of columns:
    first pair = iLoci as annotated, second pair = randomly distributed
    first value = frequency, second value = genes per miLocus

Amel
----
  23 2	  30 2
  20 3	   9 3
   4 4	   5 4
   2 5	   2 5
   5 6	   3 6
   3 7	   1 7
   3 8	   1 8
   1 10	   1 9
   1 11
   1 12

Bter
----
  17 2	  43 2
  16 3	  13 3
   8 4	   4 4
   4 5	   1 5
   5 6	   1 11
   1 7
   2 8
   1 9
   3 10
   1 12
   1 14

Hsal
----
  20 2	  43 2
  12 3	   7 3
  10 4	   4 4
   4 6	   1 6
   2 7	   1 7
   1 9
   1 10
   3 11
   1 12
   1 14

Cflo
----
  22 2	  28 2
  19 3	   8 3
  11 4	   3 4
   3 5	   1 5
   1 6	   1 9
   7 7	   1 11
   1 9
   1 10

Pdom
----
  25 2	  43 2
  25 3	   2 3
   7 4	   2 4
  11 5
   2 6
   4 7
   3 8
   1 9
   1 23

Nvit
----
  18 2	  57 2
   8 3	  16 3
  13 4	   8 4
  10 5	   1 5
   1 6	   1 6
   5 7	   1 7
   2 8	   1 8
   1 9	   1 10
   5 10
   1 11
   1 12
   1 13
   1 17
   1 22

Dmel
----
  23 2	 102 2
  20 3	  34 3
  11 4	  10 4
   7 5	  11 5
   9 6	   4 6
   4 7	   1 7
   1 8	   1 9
   2 9	   1 14
   1 10	   1 20
   1 11
   1 12
   5 15
   2 16
   3 18
   1 19
   1 24
   1 36
   1 40
   1 41

Atha
----
  99 2	  94 2
  46 3	  42 3
  36 4	  22 4
  19 5	  17 5
  14 6	   5 6
  10 7	   2 7
   8 8	   1 8
   2 9	   4 9
   2 10	   5 10
   2 11	   7 11
   2 12	   1 12
   3 13	   1 13
   1 14	   1 18
   4 15	   1 21
   2 16	   1 29
   2 17	   2 40
   1 18	   1 48
   1 19	   1 73

Bdis
----
  52 2	  38 2
  16 3	   3 3
  10 4	   1 4
   4 5	   1 5
   2 6
   1 7
   1 13

Osat
----
  59 2	  35 2
  19 3	   1 3
   8 4	   1 4
   3 5	   1 5

Xtro
----
  14 2	  10 2
   1 3	   1 3
   2 6	   1 5

Drer
----
  20 2	  14 2
   4 3	   1 4
   1 4

Btau
----
  12 2	  13 2
   2 3	   1 3
   1 4	   1 4
   1 5	   1 5
   1 6

Mmus
----
  19 2	  22 2
   7 3	   3 3
   1 4	   1 4
   2 5	   2 5
   1 9
   1 10
   1 11	
```

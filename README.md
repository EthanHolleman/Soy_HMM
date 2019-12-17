# Soy_HMM

Here I am experimenting with the HMM library in R and combining with some python scripts that I am using to come up with transition and initial emission probabilities using *Glycine Max* transportable element libraries, specifically the Gypsy Superfamily, and the 2010 reference assembly. 

## Initial Model
![First Model](https://user-images.githubusercontent.com/45807040/71016541-ea972000-20ba-11ea-86e8-c1777f9e4acb.png)  
 Transition probabilities between gnomic sequence and either intact or solo element states where calculated based on the proportion of total bases in solo or intact elements vs in genomic sequences. The basic outlines of the calculations are shown below.
```
G = sum(length of all genomic sequence)  # genomic seq = non-solo and non-intact seq
S = sum(length of all solo elements)
I = sum(length of all intact elements)

Genomic → Genomic = G – S – I / G
Genomic → Solo = G – S / G
Genomic → Intact = G – I / G
```
Since it is extremely rare for two elements to be directly adjacent (not considering insertions into another element) there is no transition possible from Solo → Intact or vice versa. The rest of the transitions where not calculated with any formula and just filled in by intuition based on the overall proportion of each type of element in the soybean genome.  
Emission probabilities where calculated from the proportion of each nucleotide in a given state. Ambiguous characters (N) where included in the proportion since repetitive elements are more difficult to sequence, so my thinking was that a higher proportion of Ns would be observed compared to the genomic sequence but the opposite was true. This is likely because regions that are just Ns are not going to be classified as transposable elements and so disproportionate amount of Ns are found in the genomic sequence. 

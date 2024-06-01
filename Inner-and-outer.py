import numpy as NP

Array1 = NP.array(input().split(), int)
Array2 = NP.array(input().split(), int)
print(NP.inner(Array1, Array2), NP.outer(Array1, Array2), sep="\n")
input()
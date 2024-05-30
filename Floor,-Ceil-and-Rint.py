import numpy as NP

NP.set_printoptions(legacy="1.13")
Array = NP.array(input().split(), float)
print("{0}\n{1}\n{2}".format(NP.floor(Array), NP.ceil(Array), NP.rint(Array)))
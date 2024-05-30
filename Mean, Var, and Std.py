import numpy as NP

N, M = input().split()
Array = NP.array([input().split() for _ in range(int(N))], int)
print(NP.mean(Array, axis=1))
print(NP.var(Array, axis=0))
print(NP.around(NP.std(Array, axis=None), decimals=11))
input()
import numpy as NP

N, M = input().split()
Array = NP.array([input().split() for _ in range(int(N))], int)
print(NP.max(NP.min(Array, axis=1)))
input()
import numpy as np

N = tuple(map(int, input().split()))
print("{0}\n{1}".format(np.zeros(N, dtype=int), np.ones(N, dtype=int)))
input()
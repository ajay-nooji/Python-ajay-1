import numpy as np

N, M, P = map(int, input().split())
Array1 = np.array([input().split() for _ in range(N)], int)
Array2 = np.array([input().split() for _ in range(M)], int)
print(np.concatenate((Array1, Array2), axis=0))
input()
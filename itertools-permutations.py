from itertools import permutations

S, k = input().split()
[print("".join(I)) for I in sorted(list(permutations(S, int(k))))]
input()
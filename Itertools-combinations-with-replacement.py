from itertools import combinations_with_replacement

S, k = input().split()
for I in sorted(list(combinations_with_replacement("".join(sorted(S)), int(k)))):
    print("".join(I))
input()
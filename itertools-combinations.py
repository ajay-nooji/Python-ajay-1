from itertools import combinations

S, k = input().split()
for i in range(int(k)):
    for j in sorted(list(combinations("".join(sorted(S)), i + 1))):
        print("".join(j))
input()
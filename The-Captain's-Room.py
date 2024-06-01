F, R = int(input()), list(map(int, input().split()))
print(((sum(set(R)) * F - sum(R))) // (F - 1))
input()
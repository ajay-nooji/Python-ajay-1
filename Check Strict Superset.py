A = set(input().split())
print(all([A.issuperset(input().split()) for _ in range(int(input()))]))
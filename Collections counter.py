from collections import Counter

_, C = input(), Counter(map(int, input().split()))
Revenue = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if C[size]:
        Revenue += int(price)
        C[size] -= 1
print(Revenue)
input()
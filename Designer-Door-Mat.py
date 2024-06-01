M, N = map(int, input().split())
P = ".|."
[print((P * I).center(N, "-")) for I in range(1, M, 2)]
print("WELCOME".center(N, "-"))
[print((P * (M - I - 1)).center(N, "-")) for I in range(1, M, 2)]
input()
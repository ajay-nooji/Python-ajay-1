x, y, z, n = int(input()), int(input()), int(input()), int(input())
print(
    [
        [i, j, k]
        for i in range(0, x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
)
input()
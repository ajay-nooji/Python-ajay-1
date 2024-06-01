cube = lambda x: x**3


def fibonacci(n):
    L = [0, 1]
    for _ in range(0, n - 2):
        L.append(L[-1] + L[-2])
    return L[0:n]


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    input()
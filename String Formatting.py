def print_formatted(num):
    [
        print("{0:{L}} {0:{L}o} {0:{L}X} {0:{L}b}".format(I, L=len(bin(num)[2:])))
        for I in range(1, num + 1)
    ]


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
    input()
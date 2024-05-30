M, A, N, B = (
    int(input()),
    set(map(int, input().split())),
    int(input()),
    set(map(int, input().split())),
)
print(*sorted(A.symmetric_difference(B)), sep="\n")
input()
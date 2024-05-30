n, S = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    eval("S.{0}({1})".format(input().split()[0], set(map(int, input().split()))))
print(sum(S))
input()
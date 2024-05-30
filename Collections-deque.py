from collections import deque

d = deque()
for _ in range(int(input())):
    cmd = input().split()
    if len(cmd) == 1:
        eval("d.{0}()".format(*cmd))
    else:
        eval("d.{0}({1})".format(*cmd))
print(*d, sep=" ")
input()
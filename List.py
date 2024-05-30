N = int(input())
arr = []
for i in range(N):
    cmd = list(input().split())
    if cmd[0] == "insert":
        i = int(cmd[1])
        e = int(cmd[2])
        arr.insert(i, e)
    elif cmd[0] == "print":
        print(arr)
    elif cmd[0] == "remove":
        try:
            arr.remove(int(cmd[1]))
        except:
            continue
    elif cmd[0] == "append":
        arr.append(int(cmd[1]))
    elif cmd[0] == "sort":
        arr.sort()
    elif cmd[0] == "pop":
        arr.pop()
    elif cmd[0] == "reverse":
        arr = arr[::-1]
input()

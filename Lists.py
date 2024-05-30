arr = [] 
for _ in range(int(input())): 
    cmd = input().split() 
    if cmd[0] == "print": 
        print(arr) 
    elif cmd[0] == "insert": 
        eval("arr.{0}({1},{2})".format(*cmd)) 
    else: 
        eval("arr.{0}({1})".format(*cmd, "")) 
input() 
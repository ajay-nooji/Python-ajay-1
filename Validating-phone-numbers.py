import re

for _ in range(int(input())):
    PN = input()
    if re.match("^7|8|9", PN) and re.fullmatch(r"\d+", PN) and len(PN) == 10:
        print("YES")
    else:
        print("NO")
input()
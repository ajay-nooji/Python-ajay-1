_, L = int(input()), input().split()
if all([int(I) > 0 for I in L]):
    print(any([J == J[::-1] for J in L]))
else:
    print(False)
input()
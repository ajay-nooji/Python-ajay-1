from collections import namedtuple

N = int(input())
Sum_marks = 0
Students = namedtuple("Students", input().split())
for _ in range(N):
    Student1 = Students(*input().split())
    Sum_marks += float(getattr(Student1, "MARKS"))
print("%.2f" % (Sum_marks / N))
input()

'''
N, Index = int(input()), input().split().index("MARKS")
print("%.2f" % (sum([int(input().split()[Index]) for _ in range(N)]) / N))
'''
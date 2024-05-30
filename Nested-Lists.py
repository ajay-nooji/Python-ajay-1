marks = []
for _ in range(0, int(input())):
    marks.append([input(), float(input())])
print(
    *sorted(
        [
            name
            for name, mark in marks
            if mark == sorted(list(set([mark for name, mark in marks])))[1]
        ]
    ),
    sep="\n"
)
input()
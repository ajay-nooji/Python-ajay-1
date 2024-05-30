if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.items():
        if i[0] == query_name:
            avg = sum(i[1]) / len(i[1])
            print("%.2f" % avg)
input()
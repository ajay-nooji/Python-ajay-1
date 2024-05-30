import numpy

n = int(input())
Array1 = numpy.array([input().split() for _ in range(n)], int)
Array2 = numpy.array([input().split() for _ in range(n)], int)
print(numpy.matmul(Array1, Array2))
input()
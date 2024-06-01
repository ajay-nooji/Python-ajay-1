import numpy

N, M = input().split()
Array = numpy.array([input().split() for _ in range(int(N))], int)
Sum = numpy.sum(Array, axis=0)
print(numpy.prod(Sum))
input()
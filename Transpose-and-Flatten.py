import numpy

N, M = map(int, input().split())
Array = numpy.array([input().split() for _ in range(N)], int)
print("{0}\n{1}".format(numpy.transpose(Array), Array.flatten()))
input()
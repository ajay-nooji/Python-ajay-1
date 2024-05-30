import numpy

N, M = input().split()
Array1 = numpy.array([input().split() for _ in range(int(N))], int)
Array2 = numpy.array([input().split() for _ in range(int(N))], int)
print(numpy.add(Array1, Array2))
print(numpy.subtract(Array1, Array2))
print(numpy.multiply(Array1, Array2))
print(numpy.floor_divide(Array1, Array2))
print(numpy.mod(Array1, Array2))
print(numpy.power(Array1, Array2))
input()
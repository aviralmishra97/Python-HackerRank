import numpy
dimensions = tuple(map(int, input().split()))
print(numpy.eye(dimensions[0], dimensions[1], k=0))

or 
import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))

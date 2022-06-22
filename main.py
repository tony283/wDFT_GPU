import cupy as cp
import numpy as np

a = cp.array([[1,2,3],[2,3,4],[3,3,1]])
print(a)
b = a@a
#print(b)
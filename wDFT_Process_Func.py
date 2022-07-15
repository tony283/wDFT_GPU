import ctypes
import cupy as cp
from numpy.ctypeslib import ndpointer

def ReadFile(_Settings:dict):
    
    _Settings['basis'] = 'STO-3G'
    return 0

def SearchBasis(_Settings:dict):
    c_func = ctypes.CDLL("lib/wDFT.dll")
    if(_Settings['basis'].lower() == 'sto-3g'):
        return ((2.22766,0.40577,0.1098175),\
            (0,0,0),\
            (0,0,0),\
            (0.154321,0.535328,0.444635))
            

def CalculateOverlap(c_func, _Settings:dict):
    basis = SearchBasis(_Settings)
    m = len(basis[0])
    m2 = m* m
    Sab = c_func.Sab
    Sab.restype = ndpointer(dtype = ctypes.c_double, shape =(m,m))
    a = Sab((ctypes.c_double*m)(*basis[0]) ,(ctypes.c_int*m)(*basis[1]),(ctypes.c_int*m)(*basis[2]),m)
    a= cp.array(a)
    print(a)
    return a

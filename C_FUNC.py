from calendar import c
import ctypes
def SetCFunc(c_func):
    c_func.S_ss.restype = ctypes.c_double
    c_func.S_sp.restype = ctypes.c_double
    c_func.S_pxpx.restype = ctypes.c_double
    c_func.S_pxpy.restype = ctypes.c_double
    c_func.S_sp.restype = ctypes.c_double


def S_ss(a,b,rab,c_func):
    return c_func.S_ss(ctypes.c_double(a),ctypes.c_double(b),ctypes.c_double(rab))

def S_sp(a,b,rab,rab_D, c_func):
    return c_func.S_ss(ctypes.c_double(a),ctypes.c_double(b),ctypes.c_double(rab),ctypes.c_double(rab_D))

def S_pxpx(a,b,rab,rab_D,c_func):
    return c_func.S_ss(ctypes.c_double(a),ctypes.c_double(b),ctypes.c_double(rab),ctypes.c_double(rab_D))

def S_pxpy(a,b,rab,rab_D1, rab_D2, c_func):
    return c_func.S_ss(ctypes.c_double(a),ctypes.c_double(b),ctypes.c_double(rab),ctypes.c_double(rab_D1),ctypes.c_double(rab_D2))
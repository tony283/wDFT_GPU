# Copyright Lin RF
# wDFT is a GPU-accelerated DFT program running on windows.
# The aim of wDFT is to fully utilize GPU to make commercial computer possible to calculate DFT on windows.
# The advantage is that the computer only needs a good GPU and the calculation is totally free. 
# Also, we aim to simplize the manipulation on DFT to make it easy to use.
import cupy as cp
import numpy as np
import wDFT_Process_Func as wF
import ctypes
import STO_NG as sto
from numpy.ctypeslib import ndpointer
import C_FUNC
c_func = ctypes.CDLL("lib/wDFT.dll")
C_FUNC.SetCFunc(c_func)
# Basic selection of basis, task and functional
_Settings = dict()
_Settings['basis'] = 'STO-3G'
_Settings['functional'] = 'HF'
_Settings['task'] = 'sp'
_Settings['rotation'] = 1
_Settings['charge'] = 0
_Settings['coord'] = cp.array([[0,0,0],[1.4,0,0]],dtype=ctypes.c_double)
_Settings['element'] = [1,1]
print(_Settings['coord'][1])
## 录入原子轨道
orbits = []
for i in range(len(_Settings['element'])):
    orbits.extend(sto.Generate_One_Atom_Orbits(_Settings['coord'][i],_Settings['basis'],_Settings['element'],c_func)) 
orbit_num = len(orbits)
## 求得重叠积分
S_overlap = sto.Overlap_Matrix(orbit_num,orbits,c_func)

print("Overlap Matrix initialized:\n",S_overlap)



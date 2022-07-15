# Copyright Lin RF
# wDFT is a GPU-accelerated DFT program running on windows.
# The aim of wDFT is to fully utilize GPU to make commercial computer possible to calculate DFT on windows.
# The advantage is that the computer only needs a good GPU and the calculation is totally free. 
# Also, we aim to simplize the manipulation on DFT to make it easy to use.
from turtle import shape
import cupy as cp
import numpy as np
import wDFT_Process_Func as wF
import ctypes
from numpy.ctypeslib import ndpointer
c_func = ctypes.CDLL("lib/wDFT.dll")

# Basic selection of basis, task and functional
_Settings = dict()
_Settings['basis'] = 'STO-3G'
_Settings['functional'] = 'HF'
_Settings['task'] = 'sp'
_Settings['rotation'] = 1
_Settings['charge'] = 0
_Settings['coord'] = cp.zeros((1,1))
_Settings['element'] = []



print(_Settings)

## First step: Calculate Overlap
a = wF.CalculateOverlap(c_func, _Settings)
print(type(a))
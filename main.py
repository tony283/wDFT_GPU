# Copyright Lin RF
# wDFT is a GPU-accelerated DFT program running on windows.
# The aim of wDFT is to fully utilize GPU to make commercial computer possible to calculate DFT on windows.
# The advantage is that the computer only needs a good GPU and the calculation is totally free. 
# Also, we aim to simplize the manipulation on DFT to make it easy to use.
import cupy as cp
import numpy as np
import wDFT_Process_Func as wF


# Basic selection of basis, task and functional
_Settings = dict()
_Settings['basis'] = 'a'
_Settings['functional'] = 'a'
_Settings['task'] = 'sp'
_Settings['rotation'] = 1
_Settings['charge'] = 0
_Settings['coord'] = cp.zeros((1,1))
_Settings['element'] = []


wF.ReadFile(_Settings)
wF.EnergyCalculate(_Settings)
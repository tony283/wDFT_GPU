import ctypes
import math
import numpy as np
import cupy as cp
def Dic_GTO(n, orbit_name):
    if(orbit_name=='1s'):
        return [[2.22766,0.40577,0.1098175],\
            [0,0,0],\
            [0,0,0],\
            [0.154321,0.535328,0.444635]]
    
    




class STO():
    def __init__(self, n , orbit_para, position,orbit_name):
        self.n = n
        package = Dic_GTO(n,orbit_name)
        self.position = position
        self.coeff = package[3]
        self.alpha = [orbit_para*orbit_para*_ for _ in package[0]]
        self.l = package[1]
        self.direction = package[2]

def Generate_One_Atom_Orbits(position, basis_name, element,c_func):
    if(basis_name.lower() == "sto-3g"):
        a = [STO(3,Dic_Coord_num(element),position,'1s')]
        return a


def Dic_Coord_num(element):
    return 1.24

def Distance(pos1,pos2):
    a=0
    for i in range(3):
        a+= (pos1[i]-pos2[i])*(pos1[i]-pos2[i])
    return math.sqrt(a)

def Rab_D(pos1,pos2,direction):
    return abs(pos1[direction]-pos2[direction])

def Overlap(STO1:STO,STO2:STO, c_func):
    add= 0
    Rab = (ctypes.c_double)(Distance(STO1.position,STO2.position))
    for i in range(STO1.n):
        for j in range(STO2.n):
            if(STO1.l[i]==0 and STO2.l[j]==0):
                temp = c_func.S_ss((ctypes.c_double)(STO1.alpha[i]),(ctypes.c_double)(STO2.alpha[j]),(ctypes.c_double)(Rab))
                add += temp*STO1.coeff[i]*STO2.coeff[j]
            elif(STO1.l[i]==0 and STO2.l[j]==1):
                direction = STO2.direction[j]
                temp = c_func.S_sp((ctypes.c_double)(STO1.alpha[i]),(ctypes.c_double)(STO2.alpha[j]),(ctypes.c_double)(Rab),(ctypes.c_double)(Rab_D(STO1.position,STO2.position,direction)))
                add += temp*STO1.coeff[i]*STO2.coeff[j]
            elif(STO1.l[i]==1 and STO2.l[j]==0):
                direction = STO1.direction[i]
                temp = c_func.S_sp((ctypes.c_double)(STO2.alpha[j]),(ctypes.c_double)(STO1.alpha[i]),(ctypes.c_double)(Rab),(ctypes.c_double)(Rab_D(STO1.position,STO2.position,direction)))
                add += temp*STO1.coeff[i]*STO2.coeff[j]
            elif(STO1.l[i]==1 and STO2.l[j]==1):
                if(STO1.direction[i]==STO2.direction[j]):
                    direction =STO1.direction[i]
                    temp = c_func.S_pxpx((ctypes.c_double)(STO2.alpha[j]),(ctypes.c_double)(STO1.alpha[i]),(ctypes.c_double)(Rab),(ctypes.c_double)(Rab_D(STO1.position,STO2.position,direction)))
                    add += temp*STO1.coeff[i]*STO2.coeff[j]
                elif(True):
                    direction1,direction2 = STO1.direction[i],STO2.direction[j]
                    temp = c_func.S_pxpy((ctypes.c_double)(STO2.alpha[j]),(ctypes.c_double)(STO1.alpha[i]),(ctypes.c_double)(Rab)\
                        ,(ctypes.c_double)(Rab_D(STO1.position,STO2.position,direction1)),(ctypes.c_double)(Rab_D(STO1.position,STO2.position,direction2)))
                    add += temp*STO1.coeff[i]*STO2.coeff[j]
    return add

            
def Overlap_Matrix(sto_num,sto_list, c_func):
    l = []
    for i in range(sto_num):
        for j in range(sto_num):
            l.append(Overlap(sto_list[i],sto_list[j],c_func))
    overlap = np.ndarray(l).reshape((sto_num,sto_num))
    return cp.array(overlap)




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

def Generate_One_Atom_Orbits(position, basis_name, coord_num):
    if(basis_name.lower() == "sto-3g"):
        a = [STO(3,Dic_Coord_num(coord_num),position,'1s')]
        return a


def Dic_Coord_num(coord_num):
    return 1.24

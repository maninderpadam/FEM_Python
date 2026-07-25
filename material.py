import numpy as np

class Material:

    def __init__(self,E,nu,plane_stress=True):

        self.E=E
        self.nu=nu
        self.plane_stress=plane_stress

    def D(self):

        E=self.E
        nu=self.nu

        if self.plane_stress:

            D=E/(1-nu**2)*np.array([

                [1,nu,0],
                [nu,1,0],
                [0,0,(1-nu)/2]
            ])

        else:

            D=E/((1-nu)*(1-2*nu))*np.array([
                [1-nu,nu,0],
                [nu,1-nu,0],
                [0,0,(1-2*nu)/2]
            ])

        return D
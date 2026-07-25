import numpy as np

def shape_function(xi,eta):
    """
    Return the four bilinear shape function evaluate at xi and eta
    """

    N1=0.25*(1-xi)*(1-eta)
    N2=0.25*(1+xi)*(1-eta)
    N3=0.25*(1+xi)*(1+eta)
    N4=0.25*(1-xi)*(1+eta)

    return np.array([N1,N2,N3,N4])
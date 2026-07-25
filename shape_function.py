"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""

import numpy as np

def shape_function(xi: float, eta: float):
    N1 = 0.25 * (1 - xi) * (1 - eta)
    N2 = 0.25 * (1 + xi) * (1 - eta)
    N3 = 0.25 * (1 + xi) * (1 + eta)
    N4 = 0.25 * (1 - xi) * (1 + eta)

    return N1,N2,N3,N4


def shape_function_derivatives(xi: float, eta: float):
    """
    Computes the partial derivatives of 4-node bilinear isoparametric 
    shape functions with respect to natural coordinates (xi, eta).

    Bilinear shape functions:
        N1 = 0.25 * (1 - xi) * (1 - eta)
        N2 = 0.25 * (1 + xi) * (1 - eta)
        N3 = 0.25 * (1 + xi) * (1 + eta)
        N4 = 0.25 * (1 - xi) * (1 + eta)
    """
    # dN / d(xi)
    dN_dxi = np.array([
        -0.25 * (1 - eta),
         0.25 * (1 - eta),
         0.25 * (1 + eta),
        -0.25 * (1 + eta)
    ])

    # dN / d(eta)
    dN_deta = np.array([
        -0.25 * (1 - xi),
        -0.25 * (1 + xi),
         0.25 * (1 + xi),
         0.25 * (1 - xi)
    ])

    return dN_dxi, dN_deta
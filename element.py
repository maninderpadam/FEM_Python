"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""

import numpy as np
from shape_function import shape_function_derivatives
from gauss import gauss_points

def jacobian(element,xi,eta):
    """
    Computes the Jacobian matrix of one element.

    Parameters
    ----------
    element : Element object
    xi, eta : Natural coordinates

    Returns
    -------
    J : 2x2 Jacobian matrix
    """
    dN_dxi, dN_deta=shape_function_derivatives(xi,eta)

    x=np.array([node.x for node in element.nodes])
    y=np.array([node.y for node in element.nodes])

    dx_dxi=np.dot(dN_dxi,x)
    dx_deta=np.dot(dN_deta,x)

    dy_dxi=np.dot(dN_dxi,y)
    dy_deta=np.dot(dN_deta,y)

    print("xi =", xi)
    print("eta =", eta)

    print("dN_dxi =", dN_dxi)
    print("dN_deta =", dN_deta)

    J=np.array([
        [dx_dxi, dy_dxi],
        [dx_deta, dy_deta]
    ])

    return J

def global_derivatives(element, xi, eta):
    """
    Compute dN/dx and dN/dy for a 4-node quadrilateral.
    """

    dN_dxi, dN_deta = shape_function_derivatives(xi, eta)

  
    J = jacobian(element, xi, eta)


    invJ = np.linalg.inv(J)

    dN_nat = np.vstack((dN_dxi, dN_deta))

    dN_global = invJ @ dN_nat

    dN_dx = dN_global[0, :]
    dN_dy = dN_global[1, :]

    return dN_dx, dN_dy

def jacobian_inverse(J):
    """
    Compute determinant and inverse of the Jacobian.
    """

    detJ = np.linalg.det(J)
    invJ = np.linalg.inv(J)

    return detJ, invJ


def B_Matrix(dN_dx, dN_dy):

    B=np.zeros(3,8)

    for i in range(4):

        col=2*i
        B[0,col]=dN_dx[i]
        B[1,col+1]=dN_dy[i]
        B[2,col]=dN_dy[i]
        B[2,col+1]=dN_dx[i]

    return B

def element_stiffness(element,material):

    Ke=np.zeros((8,8))
    points,weights=gauss_points()
    for (xi,eta), w in zip(points,weights):

        print(f"Gauss Point: {xi}, {eta}")

        # 1. Compute Jacobian
        J=jacobian(element,xi,eta)

        # 2. Compute inverse Jacobian
        detJ, invJ=jacobian_inverse(J)

        # 3. Compute global derivatives
        dN_dx,dN_dy=global_derivatives(element,xi,eta)

        # 4. Build B matrix
        B=B_Matrix(dN_dx,dN_dy)

        # 5. Get D matrix
        D=material.D()

        # 6. Add contribution to Ke
        Ke += B.T @ D @ B * detJ * w

    return Ke



"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""
from dof import DOFManager

from gauss import gauss_points


import numpy as np

from element import (
    jacobian,
    jacobian_inverse,
    global_derivatives,
    B_Matrix
)


def element_displacement(element, U, dof_manager):
    """
    Extract element displacement vector from the global displacement vector.

    Parameters
    ----------
    element : Element
    U : Global displacement vector
    dof_manager : DOFManager

    Returns
    -------
    Ue : ndarray (8,)
    """

    LM = dof_manager.get_element_dofs(element)

    Ue = U[LM]

    return Ue


def compute_strain(element, Ue, xi, eta):
    """
    Compute strain at one Gauss point.

    Parameters
    ----------
    element : Element
    Ue : Element displacement vector
    xi : Natural coordinate
    eta : Natural coordinate

    Returns
    -------
    strain : ndarray (3,)
    """

    # Jacobian
    J = jacobian(element, xi, eta)

    # Inverse Jacobian
    detJ, invJ = jacobian_inverse(J)

    # Shape function derivatives in global coordinates
    dN_dx, dN_dy = global_derivatives(invJ, xi, eta)

    # B matrix
    B = B_Matrix(dN_dx, dN_dy)

    # Strain
    strain = B @ Ue

    return strain


def element_strains(element, Ue):
    """
    Compute strains at all Gauss points.

    Returns
    -------
    strains : list
    """

    strains = []

    points, weights = gauss_points()

    for (xi, eta), weight in zip(points, weights):

        strain = compute_strain(
            element,
            Ue,
            xi,
            eta
        )

        strains.append(strain)

    return strains


def compute_stress(material, strain):
    """
    Compute stress from Hooke's law.

    Parameters
    ----------
    material : Material
    strain : ndarray (3,)

    Returns
    -------
    stress : ndarray (3,)
    """

    D = material.D()

    stress = D @ strain

    return stress


def element_stresses(element, material, Ue):
    """
    Compute stresses at all Gauss points.

    Returns
    -------
    stresses : list
    """

    stresses = []

    strains = element_strains(element, Ue)

    for strain in strains:

        stress = compute_stress(
            material,
            strain
        )

        stresses.append(stress)

    return stresses
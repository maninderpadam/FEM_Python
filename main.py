"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com
Created: July 2026
#################################################################################
"""

import numpy as np

# Mesh
from mesh import Node, Element, Mesh

# DOF
from dof import DOFManager

# Material
from material import Material

# Element
from element import element_stiffness

# Assembly
from assembly import assemble

# Boundary Conditions
from boundary_conditions import apply_boundary_conditions

# Solver
from solver import solve

# Post Processing
from postprocessing import (
    element_displacement,
    element_strains,
    element_stresses,
    element_von_mises
)

###############################################################################
# CREATE MESH
###############################################################################

mesh = Mesh()

# Nodes
n1 = Node(1, 0.0, 0.0)
n2 = Node(2, 1.0, 0.0)
n3 = Node(3, 1.0, 1.0)
n4 = Node(4, 0.0, 1.0)

mesh.add_nodes(n1)
mesh.add_nodes(n2)
mesh.add_nodes(n3)
mesh.add_nodes(n4)

# Element
e1 = Element(1, [n1, n2, n3, n4])

mesh.add_element(e1)

###############################################################################
# DOF NUMBERING
###############################################################################

dof = DOFManager(mesh)

dof.assign_dofs()

###############################################################################
# MATERIAL
###############################################################################

material = Material(
    E=210e9,
    nu=0.3,
    plane_stress=True
)

###############################################################################
# GLOBAL STIFFNESS MATRIX
###############################################################################

total_dofs = len(mesh.nodes) * 2

K_global = np.zeros((total_dofs, total_dofs))

###############################################################################
# ASSEMBLY
###############################################################################

for element in mesh.elements:

    Ke = element_stiffness(
        element,
        material
    )

    LM = dof.get_element_dofs(element)

    K_global = assemble(
        K_global,
        Ke,
        LM
    )

###############################################################################
# FORCE VECTOR
###############################################################################

F = np.zeros(total_dofs)

# 1000 N downward at Node 2 (Uy)

F[3] = -1000.0

###############################################################################
# BOUNDARY CONDITIONS
###############################################################################

fixed_dofs = [0, 1, 6, 7]

K_bc, F_bc = apply_boundary_conditions(
    K_global,
    F,
    fixed_dofs
)

###############################################################################
# SOLVE
###############################################################################

U = solve(
    K_bc,
    F_bc
)

###############################################################################
# PRINT DISPLACEMENTS
###############################################################################

print("\n")
print("=" * 70)
print("NODAL DISPLACEMENTS")
print("=" * 70)

for i in range(len(mesh.nodes)):

    ux = U[2 * i]
    uy = U[2 * i + 1]

    print(
        f"Node {i+1:2d} : "
        f"Ux = {ux: .6e} m    "
        f"Uy = {uy: .6e} m"
    )

###############################################################################
# POST PROCESSING
###############################################################################

print("\n")
print("=" * 70)
print("POST PROCESSING")
print("=" * 70)

for element in mesh.elements:

    print("\n")
    print("-" * 70)
    print(f"Element {element.element_id}")
    print("-" * 70)

    ###########################################################################
    # Element displacement vector
    ###########################################################################

    Ue = element_displacement(
        element,
        U,
        dof
    )

    print("\nElement Displacement Vector")

    print(Ue)

    ###########################################################################
    # Strains
    ###########################################################################

    strains = element_strains(
        element,
        Ue
    )

    ###########################################################################
    # Stresses
    ###########################################################################

    stresses = element_stresses(
        element,
        material,
        Ue
    )

    ###########################################################################
    # Von Mises
    ###########################################################################

    vm = element_von_mises(
        element,
        material,
        Ue
    )

    ###########################################################################
    # Print Results
    ###########################################################################

    for gp in range(4):

        print("\n")
        print(f"Gauss Point {gp+1}")
        print("-" * 30)

        eps_x = strains[gp][0]
        eps_y = strains[gp][1]
        gamma_xy = strains[gp][2]

        sigma_x = stresses[gp][0]
        sigma_y = stresses[gp][1]
        tau_xy = stresses[gp][2]

        print("STRAIN")

        print(f"εx      = {eps_x:.6e}")

        print(f"εy      = {eps_y:.6e}")

        print(f"γxy     = {gamma_xy:.6e}")

        print()

        print("STRESS")

        print(f"σx      = {sigma_x:.6e} Pa")

        print(f"σy      = {sigma_y:.6e} Pa")

        print(f"τxy     = {tau_xy:.6e} Pa")

        print()

        print(f"Von Mises = {vm[gp]:.6e} Pa")
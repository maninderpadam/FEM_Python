"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""

# Importing all the modules

import numpy as np

from mesh import Node, Element, Mesh
from dof import DOFManager
from material import Material
from element import element_stiffness
from assembly import assemble
from boundary_conditions import apply_boundary_conditions
from solver import solve
from boundary_conditions import apply_boundary_conditions
from postprocessing import element_displacement
from postprocessing import compute_stress,compute_strain, element_strains,element_stresses

# Create mesh

mesh=Mesh()

n1=Node(1,0,0)
n2=Node(2,1,0)
n3=Node(3,1,1)
n4=Node(4,0,1)

mesh.add_nodes(n1)
mesh.add_nodes(n2)
mesh.add_nodes(n3)
mesh.add_nodes(n4)

e1=Element(1,[n1,n2,n3,n4])

mesh.add_element(e1)

# DOF Numbering

dof=DOFManager(mesh)
dof.assign_dofs()

# Material Assignment

material = Material(
    E=210e9,
    nu=0.3,
    plane_stress=True
)

# Calculation of total DOF

total_dofs = len(mesh.nodes)*2

# Initialization of the K_global

K_global = np.zeros((total_dofs,total_dofs))

# Assembly loop

for element in mesh.elements:

    Ke=element_stiffness(element,material)
    LM=dof.get_element_dofs(element)
    K_global=assemble(K_global,Ke,LM)

#print(K_global)

# Force Vector
total_dofs = len(mesh.nodes) * 2
F=np.zeros(total_dofs)
F[3] = -1000.0

# Fixed DOF

fixed_dofs = [0,1,6,7]

K_bc, F_bc = apply_boundary_conditions(
    K_global,
    F,
    fixed_dofs
)

U = solve(K_bc,F_bc)


print("=" * 60)
print("POST PROCESSING")
print("=" * 60)

for element in mesh.elements:

    print(f"\nElement {element.element_id}")

    # Element displacement vector
    Ue = element_displacement(
        element,
        U,
        dof
    )

    print("\nElement Displacement")
    print(Ue)

    # Strains
    strains = element_strains(
        element,
        Ue
    )

    # Stresses
    stresses = element_stresses(
        element,
        material,
        Ue
    )

    for i in range(len(strains)):

        print(f"\nGauss Point {i+1}")

        print("Strain")

        print(strains[i])

        print("Stress")

        print(stresses[i])
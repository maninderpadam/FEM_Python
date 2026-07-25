"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""

from mesh import Node, Element, Mesh
from dof import DOFManager
from shape_function import shape_function, shape_function_derivatives
from element import jacobian
from gauss import gauss_points
from material import Material

mesh=Mesh()

n1=Node(1,0,0)
n2=Node(2,2,0)
n3=Node(3,2,2)
n4=Node(4,0,2)

mesh.add_nodes(n1)
mesh.add_nodes(n2)
mesh.add_nodes(n3)
mesh.add_nodes(n4)

e1=Element(1,[n1,n2,n3,n4])

mesh.add_element(e1)

dof_manager=DOFManager(mesh)
dof_manager.assign_dofs()
dof_manager.print_dofs()

element_dofs=dof_manager.get_element_dofs(e1)
print("Element DOFs:",element_dofs)

print(shape_function(0, 0))
print(shape_function(-1, -1))
print(shape_function(1, -1))
print(shape_function(1, 1))
print(shape_function(-1, 1))

J=jacobian(e1,0,0)
print("Jacobian\n", J)

points,weights=gauss_points()

for i,(xi,eta) in enumerate(points):
    print()
    print(f"point {i+1}")
    print(f"xi {xi}")
    print(f"eta {eta}")
    print(f"weight = {weights[i]}")
    print()


steel = Material(
    E=210e9,
    nu=0.3
)

print(steel.D())



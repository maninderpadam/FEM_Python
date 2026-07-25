from mesh import Node, Element, Mesh
from dof import DOFManager
from shape_function import shape_function

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

N=shape_function(0,0)
print(f"Shape functions:\n", N)


"""
dof.py
-------
Degree of Freedom (DOF) management and indexing routines for the FEM solver.

Handles global DOF enumeration across the mesh and extracts element gather 
vectors needed for global system matrix assembly.

Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
"""

class DOFManager:
    """Assigns and maps degrees of freedom for nodal unknowns (e.g., Ux, Uy)."""

    def __init__(self,mesh):
        self.mesh=mesh
        self.node_dofs={}


    def assign_dofs(self):
        """Assigns sequential global DOFs for each node in the mesh."""

        dof=0

        for node in self.mesh.nodes:

            self.node_dofs[node.id]=[dof,dof+1]

            dof+=2

        self.total_dofs=dof


    def print_dofs(self):

        """Prints the global DOF"""
        print("DOF Numbering")

        for node_id, dofs in self.node_dofs.items():
            print(f"Node {node_id}:Ux={dofs[0]},Uy={dofs[1]}")

        print(f"Total DOFs={self.total_dofs}")


    def get_element_dofs(self,element):
        """Returns ordered global DOFs corresponding to an element's nodes."""
        dofs=[]
        for node in element.nodes:
            dofs.extend(self.node_dofs[node.id])

        return dofs

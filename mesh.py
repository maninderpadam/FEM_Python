"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""


class Node:
    """Represents a spatial point with coordinates in 2D space."""

    def __init__(self,node_id,x,y):
        self.id=node_id
        self.x=x
        self.y=y

    def __repr__(self):

        return f"Node(id={self.id}, x={self.x}, y={self.y})"

class Element:
    """Represents a finite element composed of an ordered list of nodes."""

    def __init__(self, element_id,nodes):
        self.element_id=element_id
        self.nodes=nodes

    def __repr__(self):


        nodes_ids=[node.id for node in self.nodes]
        return f"Element (id={self.element_id}, nodes={nodes_ids})"

class Mesh:
    """Stores collections of nodes and elements composing the computational domain."""

    def __init__(self):
        self.nodes=[]
        self.elements=[]

    def add_nodes(self,node):

        """Adding the nodes"""
        self.nodes.append(node)

    def add_element(self,element):

        """Adding the nodes"""
        self.elements.append(element)

    def __repr__(self):

        text = "Mesh\n"

        text += "\nNodes:\n"

        for node in self.nodes:
            text += str(node) + "\n"

        text += "\nElements:\n"

        for element in self.elements:
            text += str(element) + "\n"

        return text
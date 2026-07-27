# 2D Finite Element Method (FEM) Solver in Python

A modular implementation of the **Finite Element Method (FEM)** for **2D linear elasticity** using **4-node quadrilateral (Q4) isoparametric elements**.

This project is developed from scratch in **Python** without using any external FEM libraries. The primary goal is to understand and implement the complete FEM workflow, from mesh generation to stress post-processing.

---

## Features

✔ Mesh generation

✔ Degree of Freedom (DOF) numbering

✔ Bilinear Q4 isoparametric elements

✔ Shape function implementation

✔ 2×2 Gauss numerical integration

✔ Jacobian computation

✔ B-Matrix formulation

✔ Plane Stress and Plane Strain material models

✔ Element stiffness matrix computation

✔ Global stiffness matrix assembly

✔ Boundary condition application

✔ Linear system solver

✔ Element displacement recovery

✔ Strain computation

✔ Stress computation

✔ Von Mises stress calculation

---

## Project Structure

```text
FEM_Python/
│
├── main.py
├── mesh.py
├── dof.py
├── shape_function.py
├── gauss.py
├── material.py
├── element.py
├── assembly.py
├── boundary_conditions.py
├── solver.py
├── postprocessing.py
└── README.md
```

---

## FEM Workflow

The solver follows the standard finite element procedure:

```text
Mesh
   │
   ▼
DOF Numbering
   │
   ▼
Element Stiffness Matrix
   │
   ▼
Global Assembly
   │
   ▼
Boundary Conditions
   │
   ▼
Solve KU = F
   │
   ▼
Nodal Displacements
   │
   ▼
Element Displacements
   │
   ▼
Strain
   │
   ▼
Stress
   │
   ▼
Von Mises Stress
```

---

## Mathematical Formulation

The governing equation of linear elasticity is

$$
KU = F
$$

where:

- **K** – Global stiffness matrix
- **U** – Nodal displacement vector
- **F** – External force vector

### Element Stiffness Matrix

The element stiffness matrix is computed as

$$
K_e = \int_{\Omega} B^T D B \, d\Omega
$$

where:

- **B** – Strain-displacement matrix
- **D** – Constitutive (material) matrix
- **Ω** – Element domain

The integral is evaluated numerically using **2×2 Gauss Quadrature**.

---

### Strain Recovery

The strain at each Gauss point is computed from the element displacement vector as

$$
\varepsilon = B U_e
$$

where:

- **ε** – Strain vector
- **B** – Strain-displacement matrix
- **Uₑ** – Element displacement vector

---

### Stress Recovery

The stress is obtained using Hooke's law

$$
\sigma = D\varepsilon
$$

where:

- **σ** – Stress vector
- **D** – Material constitutive matrix

---

### Von Mises Stress

The equivalent von Mises stress for plane stress is

$$
\sigma_{vm}
=
\sqrt{
\sigma_x^2
-\sigma_x\sigma_y
+\sigma_y^2
+3\tau_{xy}^2
}
$$

## Current Example

The solver currently analyses:

- One Q4 quadrilateral element
- Plane stress condition
- Linear elastic steel material
- Fixed boundary conditions
- Concentrated external load

---

## Requirements

- Python 3.11+
- NumPy

Install the required package:

```bash
pip install numpy
```

---

## Running the Solver

Clone the repository

```bash
git clone https://github.com/<your-username>/FEM_Python.git
```

Move into the project directory

```bash
cd FEM_Python
```

Run the solver

```bash
python main.py
```

---

## Example Output

```text
==========================================================
NODAL DISPLACEMENTS
==========================================================

Node 1
Ux = 0.000000e+00
Uy = 0.000000e+00

Node 2
Ux = ...
Uy = ...

...

==========================================================
POST PROCESSING
==========================================================

Element 1

Gauss Point 1

Strain
εx
εy
γxy

Stress
σx
σy
τxy

Von Mises Stress
σvm
```

---

## Future Improvements

- Multi-element mesh support
- Mesh import from Gmsh
- Distributed and pressure loads
- Body forces
- Sparse matrix assembly
- Iterative solvers
- Deformed mesh visualisation
- Stress contour plots
- VTK export for ParaView
- Nonlinear material models
- Dynamic analysis

---

## Learning Outcomes

This project demonstrates:

- Finite Element Method (FEM)
- Numerical Integration
- Linear Elasticity
- Matrix Assembly
- Scientific Computing
- Object-Oriented Programming (OOP)
- Python for Engineering Simulation

---

## Author

**Maninder Jeet Singh**

M.Sc. Computational Methods in Engineering

Otto von Guericke University Magdeburg

📧 maninder.padam@gmail.com

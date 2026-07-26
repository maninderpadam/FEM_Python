"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""

import numpy as np

def apply_boundary_conditions(K,F,fixed_dofs):

    # Apply prescribed BC's using row column modifications

    K=K.copy()
    F=F.copy()

    for dof in fixed_dofs:

        K[dof,:]=0
        K[:,dof]=0
        K[dof,dof]=1
        F[dof]=0

    return K,F

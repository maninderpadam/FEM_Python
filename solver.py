"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""

import numpy as np

def solve(K,F):

    #Solve KU=F

    U=np.linalg.solve(K,F)

    return U
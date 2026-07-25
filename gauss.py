"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""

import numpy as np

def gauss_points():

    g=1/np.sqrt(3)

    points=[
        (-g,-g),
        (g,-g),
        (g,g),
        (-g,g)
    ]

    weights=[1,1,1,1]

    return points,weights
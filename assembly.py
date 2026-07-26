"""
#################################################################################
Author: Maninder Jeet Singh
Email Id: maninder.padam@gmail.com and maninder.singh@st.ovgu.de
Created: July 2026
##################################################################################
"""


def assemble(K_global, Ke, LM):

    for i in range(len(LM)):
        for j in range(len(LM)):

            K_global[LM[i], LM[j]] += Ke[i,j]

    return K_global
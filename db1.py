# -*- coding: utf-8 -*-
"""
Created on Thu May 25 01:17:45 2023

@author: Sotiris
"""
import pandas as pd


#pernoume thn bash apo to exel kai thn metatrepoume se table kai meta thn epistrefoume sthn main

    
def basi(): 
    gr = 'C:/MyPythonProject/Dwkimes/gr.xlsx'
    citys = pd.read_excel(gr)
    
    return citys
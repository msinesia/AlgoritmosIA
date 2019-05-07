# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:44:07 2019

@author: maria.s.matias
"""

import os
os.chdir('C:/Users/maria.s.matias/Desktop/MestradoEachUsp/kaggle/titanic')

import pandas as pd

tst_dum = pd.read_csv ('tstGetDummies.csv')

new_dt_2 = pd.get_dummies(tst_dum, columns=['SEXO','PORTO'])
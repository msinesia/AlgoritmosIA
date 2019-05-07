# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:23:46 2019

@author: maria.s.matias
"""
# definir workspace
import os
os.chdir('C:/Users/maria.s.matias/Desktop/MestradoEachUsp/kaggle/titanic')
os.getcwd()

import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

#importar data set Titanic - treinamento
data_train = pd.read_csv ('train.csv')
data_test = pd.read_csv ('test.csv')

#visualizar data set
data_train.head()
data_test.head()

# remover atributos irrelevantes
data_train.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
data_test.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# converter atributos categóricos usando o método One Hot Encoding
new_data_train = pd.get_dummies(data_train)
new_data_test = pd.get_dummies(data_test)
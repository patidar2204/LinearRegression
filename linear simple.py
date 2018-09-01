# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:19:06 2018

@author: GAUTAM PATIDAR
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
epochs=1000

def main():
    
    data=pd.read_csv('data.csv',header=None).values
    rows,col=(np.shape(data))
    x=data[:,0:col-1]
    y=data[:,col-1]
    for i in range(rows):
        for j in range(col-1):
            x[i][j]=(int)(x[i][j])
        y[i]=(int)(y[i])
    x=np.asarray(x)
    y=np.asarray(y)
    app=np.ones((rows,1))
    x=np.hstack((app,x))
    X = []
    for i in range(rows):
        a = x[i][1]*x[i][1]
        X.append(a)
    
    X=np.reshape(np.transpose(X),(rows,1))
    x=np.hstack((x,X))
    
    y=np.reshape(y,(rows,1))
    theta=np.matmul(np.matmul((np.linalg.inv(np.matmul(np.transpose(x),x))),np.transpose(x)),y)
    print(theta)
main()

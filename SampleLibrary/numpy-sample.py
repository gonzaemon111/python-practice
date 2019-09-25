# -*- coding: utf-8 -*-
import numpy as np

A = np.array([[1.,3.] ,[4.,2.]]) # 行列Aの生成
B = np.array([1.,1.])   # 行列Bの生成

X = np.linalg.solve(A, B)
print( "X=\n" + str(X) )

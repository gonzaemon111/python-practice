# -*- coding:utf-8 -*-
from scipy import integrate

def f(x):
    return 3*x + 1

# 定積分(積分区間[0, 10])
ix, err = integrate.quad(f, 0, 10)
print('計算結果:', ix)
print('誤差：', err)

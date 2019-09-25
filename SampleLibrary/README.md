# Python で　主なライブラリの使い方

## 実行時の注意点

扱うパッケージが多いので、Pipfileというファイルでライブラリを管理する

```shell
$ pipenv install [ライブラリ]

$ pipenv run python ファイル名
```

参考サイト : https://qiita.com/shinshin86/items/e11c1124e3e2e74556b8

## matplotlib

![実行時のグラフ](image.png)

## scipy

信号処理や統計などの科学計算用のライブラリ
scipyではnumpyで行える配列や行列の演算を行うことができ、加えてさらに信号処理や統計といった計算ができる
NumPy ⊂ SciPy
な、関係。Scipyだけでいい気がするが世間ではNumPyが主流なのでNumPyで事が足りる機能であるならばNumPyを使うべきなのでしょう

学習/参考サイト:https://algorithm.joho.info/programming/python/scipy-integrate-quad/

```python
# -*- coding:utf-8 -*-
from scipy import integrate

def f(x):
    return 3*x + 1

# 定積分(積分区間[0, 10])
ix, err = integrate.quad(f, 0, 10)
print('計算結果:', ix)
print('誤差：', err)
```



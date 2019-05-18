# global変数について

x = 100
def sample_function():
    x = 200
    print(x) # 200が出力される
 
sample_function() # 関数内部でxの値を変更
print(x) # 100が出力される。つまり、関数の外側の値は変更されない


y = 100
def sample_function2():
    global y # global宣言 xはglobal変数であることを明示する
    y = 200
    print(y)
 
sample_function2() # 関数内部でxの値を変更
print(y) # 関数の外側の値が変更されている
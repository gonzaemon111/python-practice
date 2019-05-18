# 内部関数 2

def outer_function():
 
    x = 100
    print(x) # 100が出力される
 
    def inner_function():
        nonlocal x
        x = 200
        print(x) # 200が出力される
     
    inner_function()
    print(x) # 200が出力される
     
outer_function()
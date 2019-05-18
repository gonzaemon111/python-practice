# 内部関数

def outer_function():
    # """ 外側の関数 """
    print('outer')
 
    def inner_function():
        # """ 内側の関数 """
        print('inner')
 
    inner_function()
 
outer_function()
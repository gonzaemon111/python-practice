# lambda式 (無名関数)

func = lambda x: x % 2 == 1
 
is_odd = func(5)
print(is_odd)  # True
 
is_odd = func(6)
print(is_odd)  # False



# 高級関数

def higher_order(datas, is_target):
    # """ 高階関数のサンプル """
    for i in datas:
        if is_target(i):
            print(i)
 
def is_even(num):
    return num % 2 == 0
 
datas = [1, 102, 900, 5, 3]
higher_order(datas, is_even)
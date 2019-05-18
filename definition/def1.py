# シンプルな関数
def sample_function(x, y):
  z = x + y
  return z

print(sample_function(1, 2))
# ※ ruby との相違点は、メソッドを呼び出す前に定義しておく必要があること

# 可変長引数
# *が一つの引数は、tuple型 *が二つの引数は、dictionary型になる。

def sample_function2(arg1, *arg2):
    print(arg1, arg2)
 
sample_function2('a', 'b', 'c', 'd') # a ('b', 'c', 'd')が出力される
# 引数のリストは引数シーケンスへ、キーワード引数が引数辞書に格納されます。

def sample_function3(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)
 
sample_function3('a', 'b', 'c', 'd', key1='x', key2='y', key3='z') # a ('b', 'c', 'd') {'key1': 'x', 'key2': 'y', 'key3': 'z'}が出力される

# 戻り値
def sample_function4(a):
  return a

print(sample_function4("a"))
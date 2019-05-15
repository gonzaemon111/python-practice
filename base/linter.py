# integer
var1 = 1
print(var1)
print(type(var1))

# float
var2 = 1.0
print(var2)
print(type(var2))

# bool
var3 = True
print(var3)
print(type(var3))

# list
li = [1,2,'ho', {"hoge": "ko"} ]
print(li)
print(type(li))
print(li[0])
print(li[2])
print(li[1:3]) # index=1から3まで(3は含まれない) を抜き出す => index=1,2 => [2, 'ho']
print(li[:3]) # 前半３つを抜き出す => [1, 2, 'ho']

# tuple
tup = (1,2,'hoge')
print(tup)
print(type(tup))
print(tup[1])
# tuple に追加は不可能

# tupleとリストの変換
print(tuple(li)) # tuple型
print(list(tup)) # list型

# set型

# dictionary型
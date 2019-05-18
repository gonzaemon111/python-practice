# while文

i = 0

while i < 3:
    print(i)
    i += 1
# 0
# 1
# 2

# whileとelseの組み合わせ
k = 0

while k < 3:
  if k == 1:
    print("skip")
    k += 1
    continue
  print(k)
  k += 1
else:
  print("finish")
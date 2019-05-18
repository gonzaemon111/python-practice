# x < y	xがyより小さければTrue
# x <= y	xがyより小さいか等しければTrue
# x > y	xがyより大きければTrue
# x >= y	xがyより大きいか等しければTrue
# x == y	xとyの値が等しければTrue
# x != y	xとyの値が等しくなければTrue
# x is y	xとyが同じオブジェクトであればTrue
# x is not y	xとyが同じオブジェクトでなければTrue
# x in y	xがyに含まれていればTrue
# x not in y	xがyに含まれていなければTrue

def if_test(num):
    if num > 100:
        print('100 < num')
    elif num > 50:
        print('50 < num <= 100')
    elif num > 0:
        print('0 < num <= 50')
    elif num == 0:
        print('num == 0')
    else:
        print('num < 0')

if_test(1000)
# 100 < num

if_test(70)
# 50 < num <= 100

if_test(0)
# num == 0

if_test(-100)
# num < 0
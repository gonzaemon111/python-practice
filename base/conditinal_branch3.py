def if_test_and_not_or(num):
    if num >= 0 and not num % 2 == 0 or num == -10:
        print('num is positive odd or -10')
    else:
        print('num is NOT positive odd or -10')

if_test_and_not_or(5)
# num is positive odd or -10

if_test_and_not_or(10)
# num is NOT positive odd or -10

if_test_and_not_or(-10)
# num is positive odd or -10
'''
分数電卓
'''

from fractions import Fraction

def add(a,b):
    print('計算結果: {0} + {1} = {2}'.format(a,b,a+b))

def subtract(a,b):
    print('計算結果: {0} - {1} = {2}'.format(a,b,a-b))

def devide(a,b):
    print('計算結果: {0} / {1} = {2}'.format(a,b,a/b))

def multi(a,b):
    print('計算結果: {0} * {1} = {2}'.format(a,b,a*b))

if __name__ == '__main__':
    try:
        a = Fraction(input('分数を入力してください'))
        b = Fraction(input('分数を入力してください'))
        operation = input('希望する操作を選んで下さい。 - add,subtract,devide,multi:')
        if operation == 'add':
            add(a,b)
        if operation == 'subtract':
            subtract(a,b)
        if operation == 'devide':
            devide(a,b)
        if operation == 'multi':
            multi(a,b)
    except ValueError:
        print('無効な入力です')

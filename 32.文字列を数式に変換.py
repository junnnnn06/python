'''
数式乗算器
2式の積を計算する
'''

from sympy import expand, sympify
from sympy.core.sympify import SympifyError

def product(expr1, expr2):
    prod = expand(expr1*expr2)
    print(prod)

if __name__ == '__main__':
    expr1 = input('1つめの数を入力してください')
    expr2 = input('2つめの数を入力してください')
try:
    expr1 = sympify(expr1)
    expr2 = sympify(expr2)
except SympifyError:
    print('無効な入力です')
else:
    product(expr1, expr2)

'''
因数ファインダ
ユーザーに式の入力を求め、因数を計算し出力する
'''
from sympy import sympify
from sympy import factor, expand
from sympy import SympifyError

def factorizer(expr):
    p = factor(expr)
    print(p)


if __name__ == '__main__':
    expr = input('式を入力して下さい')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('無効な入力です')
    else:
        factorizer(expr)

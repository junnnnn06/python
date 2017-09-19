'''
ユーザーが入力した式をプロットする
'''

from sympy import Symbol, sympify, solve
from sympy.plotting import plot

def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y  = solutions[0]
    plot(expr_y)

if __name__ == '__main__':
    expr = input('xとyを用いた方程式を入力してください(例:2*x + 3*y + 3): ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('無効な入力です')
    else:
        plot_expression(expr)

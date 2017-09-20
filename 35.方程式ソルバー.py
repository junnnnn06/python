'''
グラフを使った方程式ソルバー
'''
from sympy.plotting import plot
from sympy import Symbol, sympify, solve, SympifyError

def plot_expression(expr1, expr2):
    solution = solve((expr1, expr2), dict = True)
    print('x:{0} y:{1}'.format(solution[0][x], solution[0][y]))
    
    solutions = solve(expr1, y)
    expr1_y = solutions[0]
    solutions = solve(expr2, y)
    expr2_y = solutions[0]
    plot(expr1_y, expr2_y)

if __name__ == '__main__':
    expr1 = input('x,yを用いた一次方程式を作りなさい')
    expr2 = input('x,yを用いた一次方程式を作りなさい')
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('無効な入力です')
    else:
        y = Symbol('y')
        x = Symbol('x')
        plot_expression(expr1, expr2)

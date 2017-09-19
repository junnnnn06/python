'''
xの値で級数の値の計算
級数・・・・一定の法則に従って変化する数を、一定の順に並べた数列の和
'''
from sympy import Symbol, pprint, init_printing

def print_series(n, x_value):
    init_printing(order='rev-lex')

    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)

    #xで級数評価
    series_value = series.subs({x:x_value})
    print('xの値が{0}の時、級数は{1}'.format(x_value, series_value))

if __name__ == '__main__':
    n = input('級数の個数を入力してください: ')
    x_value = input('級数の値を計算するxの値を入力して下さい: ')
    print_series(int(n), float(x_value))

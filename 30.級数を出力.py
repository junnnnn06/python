'''
級数を出力
'''

from sympy import Symbol, pprint, init_printing

def print_series(n):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)

if __name__ == '__main__':
    n = input('級数の個数を入力してください: ')
    print_series(int(n))

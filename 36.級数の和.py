'''
級数の和
'''
from sympy import summation, sympify, Symbol, pprint

def find_sum(n_term, num_terms):
    n = Symbol('n')
    s = summation(n_term, num_terms)
    pprint(s)

if __name__ == '__main__':
    n_term = sympify(input('級数の項数を入力して下さい'))
    num_terms = int(input('項数を入力してください'))

    find_sum(n_term, num_terms)

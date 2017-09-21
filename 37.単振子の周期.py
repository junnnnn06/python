'''
単振子の周期が長さによってどう変わるか求める。
'''

from sympy import FiniteSet, pi
def time_period(length):
    g = 9.8
    T = 2*pi*(length/g)**0.5
    return T

if __name__ == '__main__':
    L = FiniteSet(15,18,21,22.5,25)
    for l in L:
        t = time_period(l/100)
        print('長さ:{0}cm, 周期{1:.3f}秒'.format(float(l), float(t)))

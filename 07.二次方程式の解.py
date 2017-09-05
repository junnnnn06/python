'''
二次方程式の解
'''

def root(a,b,c):
    D = (b**2-4*a*c) ** 0.5
    X_1 = (-b + D)/(2 * a)
    X_2 = (-b - D)/(2 * a)
    print('X1:{0}'.format(X_1))
    print('X2:{0}'.format(X_2))

if __name__ == '__main__':
    print('a*X**2 + b*X + c = 0のときa,b,c,の値を求める')
    a = input('aを入力 : ')
    b = input('bを入力 : ')
    c = input('cを入力 : ')
    root(float(a),float(b),float(c))

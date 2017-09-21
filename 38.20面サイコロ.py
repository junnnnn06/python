'''
20面サイコロを降った時に素数の出る確率
'''
from sympy import FiniteSet
def probability(space, event):
    return len(event)/len(space)

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    space = FiniteSet(*range(1, 21))
    primes = []
    for num in space:
        if check_prime(num):
            primes.append(num)
    event = FiniteSet(*primes)
    p = probability(space, event)

    print('標本空間:{0}'.format(space))
    print('事象:{0}'.format(event))
    print('素数の出る確率{0:.5f}'.format(p))

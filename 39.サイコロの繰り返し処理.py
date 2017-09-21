'''
総数が20になるまでサイコロを振る
'''

import matplotlib.pyplot as plt
import random

target_score = 20

def roll():
    return random.randint(1,6)

if __name__ == '__main__':
    score = 0
    num_rolls = 0
    while score < target_score:
        die_roll = roll()
        num_rolls += 1
        print('出た目:{0}'.format(die_roll))
        score += die_roll

    print('{0}回サイコロをふった時{1}となり終了'.format(num_rolls, score))

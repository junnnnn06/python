'''
大数の法則
サイコロを100,1000,10000,100000,500000回振り、期待値を測る。
'''

import random

def roll(trial):
    rolls = []
    for i in range(trial):
        rolls.append(random.randint(1,6))
    return sum(rolls)/trial

if __name__ == '__main__':
    expected_value = 3.5
    print('期待値は{0}'.format(expected_value))

    for trial in [100,1000,10000,100000,500000]:
        ave = roll(trial)
        print('試行回数{0}, 期待値平均{1}'.format(trial, ave))

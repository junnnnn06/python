'''
持ち点がなくなるまで、何回硬貨を投げられるか
'''
import random

def play_game(start_amount):
    win_amount = 1
    loss_amount = 2

    cur_amount = start_amount
    toss = 0

    while cur_amount > 0:
        toss += 1
        tosses = random.randint(0,1)
        if tosses == 0:
            cur_amount += win_amount
            print('+1点! 現在の持ち点は{0}'.format(cur_amount))
        else:
            cur_amount -= loss_amount
            print('-1.5点! 現在の持ち点は{0}'.format(cur_amount))
    print('終了です :(持ち点は{0}. 試行回数は{1})'.format(cur_amount, toss))

if __name__ == '__main__':
    start_amount = float(input('開始時の持ち点を入力してください: '))
    play_game(start_amount)

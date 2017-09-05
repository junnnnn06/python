'''
奇数偶数自動判別プログラム
'''

def decision(a):
    for i in range(a, a + 20, 2):
        if i % 2 == 0:
            print('入力された数は偶数です')
            print(i)
        else:
            print('入力された数は奇数です')
            print(i)
if __name__ == '__main__':
    a = input('数を入力してください')
    a = float(a)
    if a.is_integer():
        decision(int(a))
    else:
        print('整数を入力してください')

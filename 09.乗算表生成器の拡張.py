'''
乗算表生成器の拡張
'''

def multi_tables(a,b):
    for i in range(1,b + 1):
        print('{0} * {1} = {2}'.format(a,i,a*i))
if __name__ == '__main__':
    try:
        a = float(input('数を入力して下さい: '))
        b = float(input('いくつの倍数まで表示しますか'))
        if not b.is_integer() or b < 0:
            print('正の整数を入力してください')
        else:
            multi_tables(a,int(b))
    except ValueError:
        print('無効な入力です')

'''
平均を計算
'''

def calcurate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N

    return mean

if __name__ == '__main__':
    donations = [100,60,70,900,100,200,500,500,503,600,1000,1200]
    mean = calcurate_mean(donations)
    N = len(donations)
    print('直近 {0} 日間の寄付金平均金額は {1}ドルです'.format(N,mean))

'''
分散と標準偏差
https://blog.apar.jp/data-analysis/3390/
'''

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean =s/N

    return mean

#平均からの偏差を求める
def find_difference(numbers):
    mean = calculate_mean(numbers)
    diff = []

    for num in numbers:
        diff.append(num-mean)
    return diff

def calculate_variance(numbers):
    diff = find_difference(numbers)
    #差の２乗を求める
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)

    #分散を求める
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

if __name__ == '__main__':
    donations = [100,60,70,900,100,200,500,500,503,600,1000,1200]
    variance = calculate_variance(donations)
    print('分散の値は:{0}'.format(variance))

    std = variance**0.5
    print('標準偏差は:{0}'.format(std))

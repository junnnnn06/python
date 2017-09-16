'''
CSVデータの活用
'''

def calculate_mean(data):
    s = sum(data)
    N = len(data)
    mean =s/N

    return mean

#平均からの偏差を求める
def find_difference(data):
    mean = calculate_mean(data)
    diff = []

    for num in data:
        diff.append(num-mean)
    return diff

def calculate_variance(data):
    diff = find_difference(data)
    #差の２乗を求める
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)

    #分散を求める
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(data)
    return variance

if __name__ == '__main__':
    data = [100,200,300,400,500,500,600,700,800,800]
    variance = calculate_variance(data)
    print('分散の値は:{0}'.format(variance))

    std = variance**0.5
    print('標準偏差は:{0}'.format(std))

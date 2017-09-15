'''
統計電卓
'''

def read_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(float(line))
    return data

def calculate_sum(data):
    sum_data = sum(data)

    return sum_data

def calculate_mean(data):
    s = sum(data)
    N = len(data)
    mean = s / N

    return mean

if __name__ == '__main__':
    data = read_data('mydata.txt')
    sum_data = calculate_sum(data)
    mean = calculate_mean(data)
    print('合計値は:{0}'.format(sum_data))
    print('平均値は:{0}'.format(mean))

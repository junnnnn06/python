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

def calculate_median(data):
    N = len(data)
    data.sort()

    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2) + 1

        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (data[m1] + data[2]) / 2

        return median

    else:
        m = (N + 1) / 2
        m = int(m1) - 1
        median = data[m]

        return median

def calculate_mode(data):
    from collections import Counter
    c = Counter(data)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

if __name__ == '__main__':
    data = read_data('mydata.txt')
    sum_data = calculate_sum(data)
    mean = calculate_mean(data)
    median = calculate_median(data)
    modes = calculate_mode(data)
    print('合計値は:{0}'.format(sum_data))
    print('平均値は:{0}'.format(mean))
    print('中央値は:{0}'.format(median))
    print('最頻値は:{0}'.format(modes))

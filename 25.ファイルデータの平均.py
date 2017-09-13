'''
ファイルデータの平均
'''

def read_number(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers

def calculate_mean(data):
    s = sum(data)
    N = len(data)
    mean = s/N

    return mean

if __name__ == '__main__':
    data = read_number('mydata.txt')
    mean = calculate_mean(data)
    print('ファイルデータの平均値は{0}'.format(mean))

'''
範囲を求める
'''

def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest - lowest

    return lowest, highest, r

if __name__ == '__main__':
    donations = [100,60,70,900,100,200,500,500,503,600,1000,1200]
    lowest, highest, r = find_range(donations)
    print('最小値は{0},最大値は{1},最大値と最小値の差は{2}'.format(lowest, highest,r))

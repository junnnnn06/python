'''
度数分布表
'''
from collections import Counter

def frq_table(scores):
    table = Counter(scores)
    numbers_freq = table.most_common()
    numbers_freq.sort()


    print('スコア\t頻度')
    for number in numbers_freq:
        print('{0}\t{1}'.format(number[0],number[1]))

if __name__ == '__main__':
    scores = [1,6,3,7,8,3,6,9,3,8,5,6,3,7,8,1,2,9]
    frq_table(scores)

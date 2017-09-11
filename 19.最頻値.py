'''
最頻値
'''

from collections import Counter

def calculate_mode(scores):
    c = Counter(scores)
    freq_scores = c.most_common()
    #c.most_common内の最も多いスコア[0]の回数[1]を[0][1]で指定
    max_count = freq_scores[0][1]

    modes = []
    for num in freq_scores:
        if num[1] == max_count:
            modes.append(num[0])
    return(modes)

if __name__ == '__main__':
    scores = [7,7,7,5,5,5,6,6,6,1,2]
    modes = calculate_mode(scores)

    print('もっとも頻度の高い数は:')
    for mode in modes:
        print(mode)

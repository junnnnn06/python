import matplotlib.pyplot as plt
import csv

def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        summer = []
        highest_correlated = []
        for row in reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))

    return summer, highest_correlated

if __name__ == '__main__':
    summer, highest_correlated = read_csv('correlate-summer.csv')
    corr = find_corr_x_y(summer,highest_correlated)
    print('もっとも高い相関は:{0}'.format(corr))
    scatter_plot(summer,highest_correlated)

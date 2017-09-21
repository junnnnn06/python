'''
ベン図を使って集合関係を可視化する
'''
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
import csv

def read_csv(filename):
    football = []
    others = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                football.append(row[0])
            if row[2] == '1':
                others.append(row[0])
    return football, others

def draw_venn(football, others):
    venn2(subsets=(football, others), set_labels=('football','Others'))
    plt.show()

if __name__ == '__main__':
    football, others = read_csv('sports.csv')
    s1 = FiniteSet(*football)
    s2 = FiniteSet(*others)
    draw_venn(s1, s2)

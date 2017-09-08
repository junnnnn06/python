'''
歩数の確認
'''

import matplotlib.pyplot as plt

def create_bar_chart(steps, labels):
    num_bars = len(steps)
    positions = range(1, num_bars + 1)
    plt.barh(positions, steps, align = 'center')
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of step walked')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    steps = [6534,7000,8900,10786,3467,5095]
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps, labels)

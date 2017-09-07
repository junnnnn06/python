'''
二次関数電卓
'''

import matplotlib.pyplot as plt

def create_graph(x,y):
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    x_values = range(-50,50,5)
    y_values = []
    for x in x_values:
        y_values.append(x**2 + 2*x + 1)
    create_graph(x_values, y_values)

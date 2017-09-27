'''
正方形に円を詰める
'''

from matplotlib import pyplot as plt

def draw_circle(x, y):
    circle = plt.Circle((x, y), radius = 0.5, fc = 'y')
    return circle

def draw_square():
    ax = plt.gca()
    square = plt.Polygon([(1,1), (5,1), (5,5), (1,5)], closed=True)
    ax.add_patch(square)
    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = draw_circle(x, y)
            ax.add_patch(c)
            x += 1.0
        y += 1.0
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    draw_square()

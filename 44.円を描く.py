'''
matplotlib 円パッチの使用
matplotlibの使用例下記参照
http://d.hatena.ne.jp/y_n_c/20091122/1258842406

・matplotlibでは、図全体をFigureと呼びます。
そして、その中にあるグラフ(複数個でも構わない)をAxes(複数形で、単数形だとAxis)と呼びます。
・またグラフのx, y軸それぞれの表示範囲を指定することができます。
axis('scaled')とするとx,y軸のスケールが同じになる。
'''
import matplotlib.pyplot as plt

def create_circle():
    circle = plt.Circle((0,0), radius = 0.5)
    return circle

def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    c = create_circle()
    show_shape(c)

'''
別図作製
'''
from sympy.geometry import Point, Circle, Triangle, Segment, Line
import numpy as np
import matplotlib.pyplot as plt

flg = plt.figure()
ax = flg.add_subplot(1,1,1)
ax.set_aspect('equal')
ax.grid()
p1 = (1,3)
p2 = (2,2)
p3 = (3,5)
ax.plot(*zip(p1, p2, p3, p1), 'ro--')
plt.show()
# ax2 = flg.add_subplot(1,2,2)

plt.show()

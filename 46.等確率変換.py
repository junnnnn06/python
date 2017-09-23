'''
２つの等確率変換を選ぶ列
'''

import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x + 1, y - 1

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x +1 , y + 1

def transform(p):
    #変換関数のリスト
    transformations = [transformation_1, transformation_2]
    #ランダム変換関数を選ぶ
    t = random.choice(transformations)
    x, y = t(p)
    return x, y

def build_trajectory(p, n):
    x = [p[0]]
    y = [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y

if __name__ == '__main__':
    p = (1,1) #始点
    n = int(input('反復回数を入力してください:'))
    x,y = build_trajectory(p, n)
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

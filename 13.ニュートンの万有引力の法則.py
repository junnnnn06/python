'''
2物体間の万有引力と距離の関係
万有引力は物質の質量に比例し、物質間の距離r2に反比例する。
'''

import matplotlib.pyplot as plt

def draw_graph(x,y):
    plt.plot(x,y,marker = 'o')
    plt.xlabel('distance in meters')
    plt.ylabel('gravitational force in newtons')
    plt.title('gravitational force and distance')
    plt.show()
def generate_F_r():
    r = range(100, 1001, 50)#距離: 近いほど大きな引力を生じる
    F = []
    G = 6.674*(10**-11)
    m1 = 0.5     #物体1
    m2 = 1.5     #物体2
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    draw_graph(r,F)
if __name__ == '__main__':
    generate_F_r()

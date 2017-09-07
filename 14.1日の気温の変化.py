'''
1日の気温の変化(2017年6月7日の東京と札幌の気温比較)
'''

import matplotlib.pyplot as plt

def draw_graph():
    tokyo_temp = (18.8,18.6,18.0,16.9,17.1,17.3,18.4,20.0,21.5,21.6,23.1,24.1,24.3,24.4,23.5,24.0,21.9,20.1,16.6,16.2,16.3,15.8,16.4,15.6)
    sapporo_temp = (9.3,8.7,8.4,8.6,9.0,9.1,9.7,11.4,14.2,13.0,13.9,15.0,15.5,15.5,14.8,14.4,14.0,13.2,12.0,12.0,11.3,10.7,10.7,9.9)
    hours = range(0,24)
    plt.yticks([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30])
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    plt.grid(which='major', color='blue', linestyle='--')
    # plt.grid(which='minor', color='black', linestyle='-')
    plt.plot(hours, tokyo_temp,  marker = 'o',label = 'Tokyo')
    plt.plot(hours, sapporo_temp, marker = 'o', label = 'Sapporo')
    plt.legend()
    plt.xlabel('24 hours')
    plt.ylabel('temperature')
    plt.title('compare temperature of Toyko and Sapporo')
    plt.axis(xmin=0,xmax=24,ymin=0,ymax=30)
    plt.show()

if __name__ == '__main__':
    draw_graph()

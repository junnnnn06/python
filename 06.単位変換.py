'''
単位変換プログラム　
'''
def print_menu():
    print('1.kmをmilesへ')
    print('2.milesをkmへ')

def km_miles():
    km = float(input('Kmを入力してください'))
    miles =  km / 1.609
    print('kmをmileに直すと...{0}になります'.format(miles))

def miles_km():
    miles = float(input('マイルを入力してください'))
    km = miles * 1.609
    print('mileをkmに直すと...{0}になります.'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input('希望の処理を選んでください')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()

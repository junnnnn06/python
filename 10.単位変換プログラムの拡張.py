'''
単位変換プログラムの拡張　
'''
def print_menu():
    print('1.kmをmilesへ')
    print('2.milesをkmへ')
    print('3.kgをpoundへ')
    print('4.摂氏を華氏へ')

def answer_select():
    print('1.終了')
    print('2.続ける')

def km_miles():
    km = float(input('Kmを入力してください'))
    miles =  km / 1.609
    print('kmをmileに直すと...{0}になります'.format(miles))

def miles_km():
    miles = float(input('マイルを入力してください'))
    km = miles * 1.609
    print('mileをkmに直すと...{0}になります.'.format(km))

def kg_pounds():
    kg =float(input('kgを入力してください'))
    pounds = kg * 2.204
    print('kgをpoundに直すと...{0}'.format(pounds))

def cel_fah():
    cel = float(input('摂氏℃を入力してください'))
    fah = cel * 33.8
    print('摂氏を華氏に直すと...{0}'.format(fah))

if __name__ == '__main__':
    print_menu()
    while True:
        choice = input('希望の処理を選んでください')
        if choice == '1':
            km_miles()
        if choice == '2':
            miles_km()
        if choice == '3':
            kg_pounds()
        if choice == '4':
            cel_fah()
        answer = input('終了しますか(y)?')
        if answer == 'y':
            break

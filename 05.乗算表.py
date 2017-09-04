'''
multiplication table printer
'''

def multi_tables(a):
    for i in range(1,11):
        print('{0} * {1} = {2}'.format(a,i,a*i))
if __name__ == '__main__':
    a = input('enter a number: ')
    multi_tables(float(a))

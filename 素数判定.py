#!/usr/bin/env python

a_num = 103

for num in range(2, a_num):
    if a_num % num == 0:
        print(a_num,'は素数ではありません')
        break
    else:
        print(a_num, 'は素数です')
        break

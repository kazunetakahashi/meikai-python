#
# File    : list0401.py
# Author  : Kazune Takahashi
# Created : 2020/5/16 23:21:36
# Powered by Visual Studio Code
#

a = int(input('a: '))
b = int(input('b: '))

a, b = sorted([a, b])

counter = a
while counter <= b:
    print(counter, end=' ')
    counter += 1

print()

#
# File    : list0417.py
# Author  : Kazune Takahashi
# Created : 5/17/2020, 1:23:14 PM
# Powered by Visual Studio Code
#

print('-' * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print('{:3d}'.format(i * j), end='')
    print()
print('-' * 27)

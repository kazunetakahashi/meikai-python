#
# File    : list0604.py
# Author  : Kazune Takahashi
# Created : 5/17/2020, 1:48:40 PM
# Powered by Visual Studio Code
#

s = input('string s:')
c = input('char c:')

print('We found char {} at '.format(c), end='')

for i in range(len(s)):
    if s[i] == c:
        print('s[{}].'.format(i))
        break
else:
    print('nowhere.')

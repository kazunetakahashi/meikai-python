#
# File    : gist.py
# Author  : Kazune Takahashi
# Created : 2020/5/16 23:03:33
# Powered by Visual Studio Code
#

a = int(input('integer a:'))
b = int(input('b:'))
c = int(input('c:'))
d = int(input('d:'))

if a:
    print('a is not zero.')
if not b:
    print('b is zero')

x = a or b or c or d
print('x = {}'.format(x))

if d % c:
    print('c is not a divisor of d.')
else:
    print('c is a divisor of d.')

print('c is', ('an odd number' if c % 2 else 'an even number'), '.')

print('The evaluation of d = {}: '.format(d), end='')
if d < 0 or d > 100:
    print('Invalid.')
elif d >= 60:
    print('Passed.')
else:
    print('Not passed.')

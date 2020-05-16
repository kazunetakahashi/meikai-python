#
# File    : list04c01.py
# Author  : Kazune Takahashi
# Created : 5/17/2020, 12:11:26 AM
# Powered by Visual Studio Code
#

import time

print('Countdown')
N = int(input('n = '))

while N >= 0:
    print(N, end=' ', flush=True)
    N -= 1
    time.sleep(1)

print()

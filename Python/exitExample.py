#!/usr/bin/python3
# Ending a program early with the sys.exit() function

import sys

while True:
    print('Type exit to exit.')
    response input()
    if response = 'exit':
        sys.exit()
    print('You typed' + response + '.')

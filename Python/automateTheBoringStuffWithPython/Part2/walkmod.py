#!usr/bin/python3

import os, pathlib
for folderName, subfolders, filenames in os.walk(path.home()):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF' + folderName + ': '  + subfolder)

    for filename in filenames:
        print('FILE INSIDE' + folderName + ':' + filename)

    print('')

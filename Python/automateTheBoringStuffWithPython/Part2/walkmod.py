#!/usr/bin/python3
# this script lists all the folds, subfolders and filename in the home dir

import os
from pathlib import Path
for folderName, subfolders, filenames in os.walk(Path.home()):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF' + folderName + ': '  + subfolder)

    for filename in filenames:
        print('FILE INSIDE' + folderName + ':' + filename)

    print('')

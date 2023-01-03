#!usr/bin/python
# program deletes all files in the home directory that
# has extention rxt

import os
from pathlib import Path
for filename in Path.home().glob('*rxt'):
    # os.unlink(filename) : this line is comment to let 
    # the user see the files to be deleted first.
    print(filename)


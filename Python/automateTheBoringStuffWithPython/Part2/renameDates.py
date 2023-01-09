#!/usr/bin/python3
# renameDates.py - Renames filenames with American MM-DD-YYY date formate
# to European DD-MM-YYYY

import shutil, os, re
# Create a regex that matches files with the American date format.
datePattern = re.compile(r""" ^(.*?)            # all text before the date
                         ((0|1)?\d)-            # one or teo degits for the month
                         ((0|1|2|3)?\d)-        # one or two digits for the day
                         ((19|20)\d\d)          # for digits for the year
                         """,re.VERBOSE)
# TODO: Loop over the files in the working directory.
# TODO: Skip files without a date.
# TODO: Get the different parts of the filename.
# TODO: Form the European-style filename.
# TODO: Get the full, absolute file paths.
# TODO: Rename the files....check automateboringstuffwithpythonpgnum261

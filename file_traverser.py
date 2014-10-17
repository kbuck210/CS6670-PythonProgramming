## CS672 - Python Programming
## Homework 3
## Kevin C. Buckley
## 9/29/14
##
## -------------------------
##  File Traverser Module
## -------------------------

import os
import time
import fnmatch
import pickle

# Use the working directory of the python code as the start directory

def traverse_dirs():
    start_dir = os.getcwd()

    # Walk the working directory to find each .txt and .log file,
    # getting their path and file contents to put in a list of tuples
    file_data = []
    for dirpath, dirs, files in os.walk(start_dir):
        for single_file in files:
            if (fnmatch.fnmatch(single_file, "*log") or
                  fnmatch.fnmatch(single_file, "*txt")):
                filename = os.path.join(dirpath, single_file)
                f = open(filename)
                file_contents = f.read()
                mod_time = time.ctime(os.path.getmtime(filename))
                fSize = os.path.getsize(filename)
                f.close()
                this_file = (os.path.abspath(single_file), file_contents, mod_time, fSize)
                file_data.append(this_file)

    p = open("raw_data.pickle", "bw")
    pickle.dump(file_data, p)
    p.close()

    return "raw_data.pickle"    # returns the filename of the stored data



            




#!/usr/bin/python
import os
import glob
import sys

for i in range(len(sys.argv) - 1):
    print(sys.argv[i + 1])
    for filepath in glob.glob('**/*' + sys.argv[i + 1], recursive=True):
        print(filepath)
        if os.path.isfile(filepath) and filepath != "source.txt":
            a = open('source.txt', 'a+')
            a.write("\n")
            a.write("################################################################\n")
            a.write(filepath + "\n")
            a.write("################################################################\n")
            a.write("\n")

            with open(filepath, "r") as file:
                for line in file:
                    a.write(line + "\n")

#!/usr/bin/python
import os
import glob
import sys
import argparse

parser = argparse.ArgumentParser(description='Source code txt.maker')
parser.add_argument("--e", nargs='+',  default=None, type=str, help="Supply file extensions")
parser.add_argument("--i", nargs='+', default=None, type=str, help="Ignore folder")
for _, value in parser.parse_args()._get_kwargs():
    if _ == 'e':
        extension = value
        print('Extensions'+str(extension))
    if _ == 'i':
        ignore = value
        print('Ignore'+str(ignore))
for i in range(len(sys.argv) - 1):
    print(sys.argv[i + 1])
    for filepath in glob.glob('**/*' + sys.argv[i + 1], recursive=True):
        print(filepath)
        if os.path.isfile(filepath) and filepath != "source.txt" and ignore[0] not in filepath:
            a = open('source.txt', 'a+')
            a.write("\n")
            a.write("################################################################\n")
            a.write(filepath + "\n")
            a.write("################################################################\n")
            a.write("\n")

            with open(filepath, "r") as file:
                for line in file:
                    a.write(line + "\n")

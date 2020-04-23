#!/usr/bin/python
import os
import glob
import sys
import argparse

parser = argparse.ArgumentParser(description='Source code txt.maker')
parser.add_argument("--e", nargs='+',  default=None, type=str, help="Supply file extensions to add to source file")
parser.add_argument("--i", nargs='+', default=None, type=str, help="Ignore folder/file from source")
for _, value in parser.parse_args()._get_kwargs():
    if _ == 'e':
        extension = value
        print('Extensions'+str(extension))
    if _ == 'i':
        ignore = value
        print('Ignore'+str(ignore))
for i in range(len(extension)):
    print(extension[i])
    for filepath in glob.glob('**/*' + extension[i], recursive=True):
        print(filepath)
        if os.path.isfile(filepath) and filepath != "source.txt":
            folders = filepath.split("/")
            print("folders"+str(folders))
            if not any(x in folders for x in ignore):
                a = open('source.txt', 'a+')
                a.write("\n")
                a.write("################################################################\n")
                a.write(filepath + "\n")
                a.write("################################################################\n")
                a.write("\n")

                with open(filepath, "r") as file:
                    for line in file:
                        a.write(line)

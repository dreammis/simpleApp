# coding=utf-8

import os

def create_dir(directory):
    if os.path.exists(directory):
        os.mkdir(directory)

def write_file(file,data):
    f = open(file,'w+')
    f.write(data)
    f.close

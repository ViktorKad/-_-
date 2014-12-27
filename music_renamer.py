#coding:cp1251

"""
# TODO: Добавить описание
"""

"""
This application can run in Python 3 and 2 (Windows 7)
Need mutagen module (http://mutagen.readthedocs.org/)
"""

import sys, os
# from mutagen.easyid3 import EasyID3
try:
    from mutagen.easyid3 import EasyID3
except ImportError:
    print ("Sorry but you don't have 'mutagen' module. Please install it.")
    exit()

def get_title(path_to_file):
    audio = EasyID3(path_to_file)
    return audio["title"]


def write_file(path_to_file, data):
    with open(path_to_file, "w+b") as _file:
        _file.write(data)


def get_data(path_to_file):
    with open(path_to_file, "rb") as _file:
        return _file.read()


def user_input(text):
    IS_PYTHON_2 = sys.version_info < (3, 0)

    if IS_PYTHON_2:
        answer = raw_input(text)
    else:
        answer = input(text)

    return answer


in_dir = "music/"
out_dir = "out/"

print ("""Default settings:
    Input directory: '%s'
    Output directory: '%s'
    """ % (in_dir, out_dir, ))

answ = user_input("Do you want change it? (yes/no or y/n):").lower()

if answ == "yes" or answ == "y":
    in_dir = user_input("Please enter new value for input directory: ")
    out_dir = user_input("Please enter new value for output directory: ")
    print ("""New settings:
    Input directory: '%s'
    Output directory: '%s'""" % (in_dir, out_dir, ))

if not os.path.isdir(in_dir):
    user_input("Error: input directory (%s) is not exist." % (in_dir, ))
    exit()

if not os.path.isdir(out_dir):
    print ("Creating '%s' directory..." % (out_dir, ))
    os.mkdir(out_dir)

print ("""------------------------
Application is started
------------------------""")

# Path to input file
path_to_in_file = None
# Path to output file
path_to_out_file = None
# Binary data from input file
data = None
# ID3 title from input file
title = None
# Input file extension
extension = None

for file_name in os.listdir(in_dir):
    path_to_in_file = os.path.join(in_dir, file_name)

    print ("'%s' file processing..." % (path_to_in_file, ))
    title = get_title(path_to_in_file)[0].strip()
    # convert non english title to right windows coding
    title = title.encode('latin1').decode("cp1251")
    extension = os.path.splitext(file_name)[-1]
    print ("\tFile reading...")
    data = get_data(path_to_in_file)

    path_to_out_file = os.path.join(out_dir, "%s%s" % (title, extension))

    print ("\t'%s' file writing..." % (path_to_out_file, ))
    write_file(path_to_out_file, data)

    print ("\tDone. New file name is '%s'" % (title, ))


print ("------------------------")
user_input("\nAll is done. Please press enter for exit...")
#!/usr/bin/env python3

import os
import magic # /!\ pip install python-magic
import sys
import getopt

# Utilisation
# -f <folder_name> indicates the folder where the operation will be done
# -a to add the extension
# -d to remove the extension
# -r recursive folder
usage="""NOM:
toggle_extension.py - Add or remove the extension of video files

USAGE:
toggle_extension.py -f <folder_name> [-a|-d] [-r]

VERSION:
1.1

OPTIONS:
-f <folder_name> specifies the folder where the operation will be done
-a add the extension
-d delete the extension
-r do the operation to the subdirectories
-h print this menu
"""

# Variables initialisation
folder = ''
op_type = ''
is_recursive = False

# Get the options
try:
    opts, args = getopt.getopt(sys.argv[1:], "adrhf:")
except Exception as e:
    print("You forgot an argument of an option")
    sys.exit(1)

# If the user do not enter any option
if (not opts):
    print(usage)

# Treat the options
for o, a in opts:
    if o == '-f':
        if (a[-1] == '/'):
            folder = a[:-1]
        else:
            folder = a
    elif o == '-a':
        op_type = 'add'
    elif o == '-d':
        op_type = 'delete'
    elif o == '-r':
        is_recursive = True
    elif o == '-h':
        print(usage)

# Check if all options are ok
if not folder:
    print("You forgot the -f option")
    sys.exit(1)
if not op_type:
    print("You forgot the -a/-r option")
    sys.exit(1)
try:
    files = os.listdir(folder)
except Exception as e:
    print(e)
    sys.exit(1)

# Test the magic librairy installed
is_python_magic = False
try:
    m = magic.open(magic.MAGIC_MIME)
except:
    is_python_magic = True

# Add or remove the extension
def toggle_extension(files, path):
    for filename in files:
        full_filename = path + filename
        is_dir = os.path.isdir(full_filename)
        if (is_dir):
            if (is_recursive):
                new_files = os.listdir(full_filename)
                toggle_extension(new_files, path + filename + '/')
        else:
            if is_python_magic:
                type_extension = magic.from_file(full_filename, mime=True)
            else:
                m = magic.open(magic.MAGIC_MIME)
                m.load()
                type_extension = m.file(full_filename).split(';')[0]
            file_type, file_extension = type_extension.split('/')
            if file_type == 'video':
                if file_extension == 'x-matroska':
                    file_extension = 'mkv'
                elif file_extension == 'x-msvideo':
                    file_extension = 'avi'
                elif file_extension == 'x-m4v':
                    file_extension = 'm4v'
                elif file_extension == 'quicktime':
                    file_extension = 'mov'
                elif file_extension == 'x-ms-wmv':
                    file_extension = 'wmv'
                elif file_extension == 'mpeg':
                    file_extension = 'mpg'
                elif file_extension == 'x-flv':
                    file_extension = 'flv'
                if (op_type == 'add'):
                    if full_filename.split(".")[-1] != file_extension:
                        new_full_filename = "%s.%s" %(full_filename, file_extension)
                    else:
                        new_full_filename = full_filename
                elif (op_type == 'delete'):
                    if full_filename.split(".")[-1] == file_extension:
                        new_full_filename = ".".join(full_filename.split(".")[:-1])
                    else:
                        new_full_filename = full_filename
                os.rename(full_filename, new_full_filename)
                print(new_full_filename)

toggle_extension(files, folder + '/')

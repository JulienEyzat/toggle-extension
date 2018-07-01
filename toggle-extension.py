#!/usr/bin/env python3

import os
import magic # /!\ pip install python-magic
import sys
import getopt

# Utilisation
# -f <folder_name> indicates the folder where the opération will be done
# -a to add the extension
# -r to remove the extension

# Variables initialisation
folder = ''
op_type = ''

# Get the options
try:
    opts, args = getopt.getopt(sys.argv[1:], "arf:")
except Exception as e:
    print("You forgot an argument of an option")
    sys.exit(1)

# Treat the options
for o, a in opts:
    if o == '-f':
        if (a[-1] == '/'):
            folder = a[:-1]
        else:
            folder = a
    elif o == '-a':
        op_type = 'add'
    elif o == '-r':
        op_type = 'remove'

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

# Add or remove the extension
for filename in files:
    full_filename = folder + '/' + filename
    type_extension = magic.from_file(full_filename, mime=True)
    file_type, file_extension = type_extension.split('/')
    if (op_type == 'add'):
        new_full_filename = full_filename.rsplit(".", 1)[0]+'.'+file_extension
    elif (op_type == 'remove'):
        new_full_filename = full_filename.rsplit(".", 1)[0]
    os.rename(full_filename, new_full_filename)
    print(new_full_filename)

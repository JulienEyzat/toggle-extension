toggle-extension - Add and remove extension of video files

# DESCRIPTION

A little command line function to rename all the only video files in a folder (and optionnaly subdirectories) with their extension or not.
It works at least for mp4, avi and mkv video formats.

# USAGE

    toggle_extension.py -f <folder_name> [-a|-d] [-r]

# OPTIONS

- `-f <directory_name>` : specifies the directory where the operation will be done
- `-a` : add the extension to all the files in the directory
- `-d` : delete the extension to all the files in the directory
- `-r` : do the operation also to the files in the subdirectories of the given directory
- `-h` : print the help menu

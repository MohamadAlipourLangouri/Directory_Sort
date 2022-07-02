import os
import pathlib
import shutil
from pathlib import Path

# Get the list of all files and directories
path = 'C://Users//MoAlipour//Desktop//sort train'
dir_list = os.listdir(path)

#get extensions of the file
for item in dir_list:
    file_extension = pathlib.Path(item).suffix
    print("File Extension: ", file_extension)
    if file_extension :
        newPath = path  + "//" + file_extension +" files"
        if not os.path.exists(newPath):
            os.makedirs(newPath)
    #move directory to the file
for item in dir_list:
    if os.path.isfile(path + "//" + item):
        source = path + "//" + item
        destination = path + "//"+ pathlib.Path(item).suffix + " files"
        dest = shutil.move(source, destination)
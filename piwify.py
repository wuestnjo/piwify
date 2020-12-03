'''
Batch rename folders and files
 - Replacing umlauts and spaces

Initially written to make big picture folder work with piwigo

'''

import os, glob, shutil, sys

path = '/mnt/u/ <big picture folder>'
suffix = '/*'
prefix = ""
k = 1

## Check if path is valid
if not os.path.isdir(path):
    print(f"{path} not a directory")
    sys.exit()
if path != path.replace(" ","-").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue"):
    print(f"{path} doesn't meet requirements")
    sys.exit()

## "Deep Field Search" for lowest directory
while list(glob.iglob(path + suffix)) != []:
    suffix += '/*'
    k += 1
suffix = '/*'

for depth in range(1, k):
    ## Create List for directories and files
    temp = list(glob.iglob(path + suffix, recursive=False))
    dirList = []
    fileList = []
    for obj in temp:
        if os.path.isdir(obj):     # adding only folders to dirList
            dirList.append(obj)      
        if os.path.isfile(obj):     # adding only files to fileList
            fileList.append(obj)                  

    ## Iterate tree top first and rename folders and files
    print(f"{path + suffix}")
    for dir in dirList:
        new_dir = dir.replace(" ","-").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
        if new_dir != dir:
            if os.path.exists(new_dir):   # destination existing?
                # TODO: os.listdir(new_dir) == [] (meaning empty) -> delete
                print(f"{suffix} folders\t CONFLICT with: {dir}")
                continue
            shutil.move(dir, new_dir)
            dir = dir.replace(path, "")
            new_dir = new_dir.replace(path, "")
            print(f" {suffix}{dir}  -->  {new_dir}")
    print(f"  {suffix}/ folders done")

    for file in fileList:
        new_name = file.replace(" ","-").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
        if new_name != file:
            os.rename(file, new_name)
            file = file.replace(path, "")
            new_name = new_name.replace(path, "")
            print(f" {suffix}{file}  -->  {new_name}")
        
    print(f"  {suffix}/ files done")

    suffix += '/*'
    prefix += " "

print("all done")
import os
import shutil
 
from PIL import Image

"""
###Sort func
Moves files into respective folders according to their extensions
"""


def resize(path):

    list_ = os.listdir(path)
    print(list_)
    os.chdir(path)
    crt = os.getcwd()
    print (crt)
	
    #Traverses to every file

    for filename in list_:
        name,ext = os.path.splitext(filename)
        print(f"working on {filename}")
        # ext = ext[1:]
        # if ext == '':
        #     continue
        # if os.path.exists(path+'/'+ext):
        #     shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)
        # else:
        #     os.makedirs(path+'/'+ext)
        #     shutil.move(path+'/'+filename, path+'/'+ext+'/'+filename)
        
        im = Image.open(path +'/'+filename)
        imR = im.resize((150,150), Image.ANTIALIAS)
        imR.save(path+'/'+filename, quality=100)

# resize("./lfw_data")


def resize2(path):
    #Set path as current working directory
    os.chdir(path)
    dest_dir = os.getcwd()
    #generator that walks over the folder tree
    walker = os.walk(dest_dir)
     
    # the first walk would be the same main directory
    # which if processed, is redundant
    # and raises shutil.Error
    # as the file already exists
     
    rem_dirs = walker
     
    for data in walker:
        for files in data[2]:
            try:
                im = Image.open(data[0] + os.sep + files)
                imR = im.resize((150,150), Image.ANTIALIAS)
                imR.save(data[0] + os.sep + files, quality=100)
                # shutil.move(data[0] + os.sep + files, dest_dir)
                # print(data[0] + os.sep + files)
            except shutil.Error:
    # to be on the safer side
                continue

resize2("./lfw_data")


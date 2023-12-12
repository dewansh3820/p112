import os
import time
import shutil

from_dir= "C:/Users/jainn/Downloads"
to_dir= "C:/Users/jainn/Pictures"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension =os.path.splitext(file_name)
    print(name)
    print(extension)

    if (extension==""):
        continue
    if extension in [ ".png",".jfif",".jpg",".jpeg",".gif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+ "/" + file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)

    
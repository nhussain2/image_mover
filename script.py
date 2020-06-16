import os 
import shutil

path = "/Users/naveedhussain/Desktop/"
# List all the files
names = os.listdir(path)
folder_name=['image','text']
# If folder does not exist, make new folder
for x in range(0,2):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])
img_count = 0
txt_count = 0
# Go through files in the file names, check if img or txt
for files in names:
    if ("png" or "jpg" or "jpeg") in files and not os.path.exists(path+"image/"+files):
        shutil.move(path+files, path+'image/'+files)
        img_count += 1
    if ".txt" in files and not os.path.exists(path+"text/"+files):
        shutil.move(path+files, path+'text/'+files)
        txt_count += 1

print("%d many image files were moved!" % img_count)
print("%d many text files were moved!" % txt_count)



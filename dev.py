# imports
import os
import pathlib


if(os.path.isdir("newDir") == False):
    os.mkdir("newDir")

print(os.getcwd())

os.chdir("newDir")

print(os.getcwd())


# now create files inside the new directory
f_name="one"
file_ext=[".txt",".java",".py",".sh"]
for i in range(4):
    # check if the files exist first
    if(os.path.isfile(f"{f_name}{file_ext[i]}") == False):
        file=f"{f_name}{file_ext[i]}"
        with open(f"{file}",mode="x+"):
            pass
        # print out their permissions too
        
        file_perm=os.stat(f"{f_name}{file_ext[i]}")
    else:
        file=f"{f_name}{file_ext[i]}"
        file_perm=os.stat(f"{f_name}{file_ext[i]}")
        print(f"{file} has {file_perm} permissions")


# we use the pathlib library to get to the currentworking directory
this_Dir= pathlib.Path(os.getcwd())
for files in this_Dir.iterdir():
    if(files.is_file):
        print(files)

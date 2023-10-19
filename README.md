# devops-assesment
Repo for devops assesment test
# devops-assesment
Repo for devops assesment test

## Executing scripts
    - Created 2 python scripting files
### Function to delete all .sh files 
    - The function takes a directory path as its argument and attempts to delete all files with a .sh extension 
    - It imports the os module to work with the file system.
    - Inside the function, it attempts to list all files and directories in the specified directory using os.listdir(directory_path)
    - It then iterates over the list of files and checks whether each item is a file (not a directory) and whether it ends with ".sh" using os.path.isfile(file_path) and file.endswith(".sh").
    - If the conditions are met for a file, it attempts to remove the file using os.remove(file_path).
### Function to check whether license/ignore exist
    - The second to check whether git ignore and license files exist
    - The function imports the os module, specifies a directory path, and then uses the os.listdir(path) function to list all the files and directories in that directory.
    - It prints a message indicating the directory whose contents are being listed.
    - If .ignore and license files exist they will be listed after the function call

## Version Control Systems
- Github
- Gitlab
- Beanstalk
- PerForce
- Apache Subversion
- AWS CodeCommit
-  Microsoft Team Foundation Server
-  Mercurial
- CVS Version Control (Concurrent Versions System)
- Bitbucket
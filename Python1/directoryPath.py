#import  the os module
import os
#specified the directory
dirctory_path = '/college'
# use the os module to list the directory
contents = os.listdir(dirctory_path)
# for item in contents:
#     #print each file and directory
#     print(item)
print(contents)
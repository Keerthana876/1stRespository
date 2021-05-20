import os
import subprocess

#func to subprocess call
def mycall(command):
    value = subprocess.call(command,shell=True)

#func to change direc
def my_changedir(my_string):
    newdir = os.chdir(my_string)

#git clone url
git_clone= "git clone https://github.com/Keerthana876/1stRespository.git"
mycall(git_clone)

#to split the url using '/' and '.' to get the repository directory
var1 = git_clone.split('/')[-1]
print(var1)
var2 = var1.split('.')[-2]
print(var2)

cwd = os.getcwd()
mycall(cwd) #call to subprocess

#combining prasent working directory and repo dic
string_cat = os.path.join(cwd,var2)
print(string_cat)
my_changedir(string_cat)#call to subprocess

#to store get log commits in file
my_call= "git log > sample.txt"
mycall(my_call)#call to subprocess






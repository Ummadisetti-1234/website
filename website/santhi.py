import os
def current():
    cwd=os.getcwd()
    print("cwd",cwd)
    print("hello")
current()   
def  file(filename):
    path=os.path.abspath(filename)
    print("path",path)
filename="sample.txt"    
file(filename)   


#coding=utf-8
'''

'''
import subprocess
import os, sys
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from getopt import getopt
#currentPath = os.getcwd() #当前路径
#vulsDir = os.listdir(currentPath) 
#print(vulsDir)
#print(currentPath+"\\vuls")
opts, args= getopt(sys.argv[1:], "hu:") 
url = ''
for op, value in opts:
    if op == '-u':
        url = value
pyfiles = []
def traversalFile(path):#遍历目录vuls下的py文件
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            traversalFile(child)
        else:
             pyfiles.append(child)
def executePy(pyfile):
    a = 'python ' + pyfile + " " + url
    p = subprocess.Popen(a, shell= True, stdout=subprocess.PIPE, bufsize = 1)
    print(p.stdout.read().decode("gbk"))

def main():
    threadsNum = 20 #线程数
    vulsPool = ThreadPool(threadsNum)
    traversalFile(os.getcwd()+"\\vuls")
    start = 0
    while(start < len(pyfiles) and len(pyfiles) > 0):
        if start+threadsNum < len(pyfiles):
            end = start+threadsNum
        else:
            end = len(pyfiles) 
        pocs = pyfiles[start : end]
        start = end
        vulsPool.map(executePy, pocs)
    vulsPool.close()
    vulsPool.join()
if __name__ == '__main__':
    main()

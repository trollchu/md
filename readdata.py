# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 22:42:34 2017

@author: Roy
"""
'''
f = open("foo.txt")             # 返回一个文件对象  
line = f.readline()             # 调用文件的 readline()方法  
while line:  
    print line,                 # 后面跟 ',' 将忽略换行符  
    # print(line, end = '')　　　# 在 Python 3中使用  
    line = f.readline()  

f.close()  
#####################

for line in open("foo.txt"):  
    print line,  
 ####################   
    
f = open("c:\\1.txt","r")  
lines = f.readlines()#读取全部内容  
for line in lines  
    print line  
############
'''
from pprint import pprint
fl=open('data.txt')
list=[]
for f in fl:
    t=f.strip()#除掉句首空格
#    print(t)
    p=t.split()#分割默认是空格
#    print(p)

    list.append(p)
    #linelist = map(int,p)# 方法一  

    # linelist = [int(i) for i in linestrlist] # 方法二  
mDic={}
pig=0
for l in list:
    if 'Masses' in l:
        pig=2
        continue
    if pig>0:
        if len(l)==0:
            pig-=1
        else:
            mDic[l[0]]=l[1]
            #pprint(l)
pprint(mDic)
num={}
flag=0
for l in list:
    if 'Atoms' in l:
        flag=1
        continue
    if flag==1 and len(l)>2:
        if mDic[l[1]] in num:
            num[mDic[l[1]]]+=1
        else:
            num[mDic[l[1]]]=1
pprint(num)



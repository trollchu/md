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
def dataOrderChanger(order,data):
    from pprint import pprint
    with open(data) as fl:
        list=[]
        for f in fl:
            t=f.strip()#除掉句首空格
            p=t.split()#分割默认是空格
            if len(p)>0:
                  list.append(p)
    #pprint(list)                  
    for i in range(len(list)):
        if list[i][0]=='Masses':
            a=i+1
        elif list[i][0]=='Atoms':
            b=i
    oDic={}
    oDic=oDic.fromkeys(order,9)#{c:1,h:2}
    for i in range(len(order)):
        oDic[order[i]]=i+1
    #pprint(oDic)

    
    
    eDic={}        
    for i in range(a,b):
        eDic[list[i][0]]=list[i][1]
    pprint(eDic)
    
    for i in range(b+1,len(list)):
        list[i][1]=oDic[eDic[list[i][1]]]
    #pprint(list)
#    pig=0
#    for l in list:
#        if 'Masses' in l:
#            pig=2
#            continue
#        if pig>0:
#            if len(l)==0:
#                pig-=1
#            else:
#                mDic[l[0]]=l[1]
#                #pprint(l)
#    pprint(mDic)
#    num={}
#    flag=0
#    for l in list:
#        if 'Atoms' in l:
#            flag=1
#            continue
#        if flag==1 and len(l)>2:
#            if mDic[l[1]] in num:
#                num[mDic[l[1]]]+=1
#            else:
#                num[mDic[l[1]]]=1
    return 0

a=dataOrderChanger(['O','N','C','H'],'data.txt')
    

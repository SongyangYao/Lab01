#####################
#author:Songyang Yao
#email:yao177@purdue.edu
#ID:ee364a08
#date:2019.01.15
#####################
import os
import sys
#problem1
def findLongest():
    index=13
    st=index
    relist=[]
    while index > 0:

        list = []
        i = index
        list.append(i)
        id = list[index - i]
        while id!=1:
            if (id%2)==0:
                id=id//2
                list.append(id)
                i=i-1
            else:
                id=3*id+1
                list.append(id)
                i=i-1
        #print(list)
        relist.append(len(list))
        index=index-1
    #print('relist:',relist)

    yy=1
    tempp=relist[0]
    inddd=yy
    while yy<len(relist):
        if relist[yy]>tempp:
            tempp=relist[yy]
            inddd=yy
            yy=yy+1
        else:
            yy=yy+1
    return st-inddd
#####
print(findLongest())
######
#problem2
def sd(a,b):
    list_a=list(str(a))
    list_b=list(str(b))
    pp=len(list_a)
    qq=len(list_b)
    jjj=0
    ij=0
    summ=0
    if pp!=qq:
        return False
    else:
        while ij <pp:
            if list_a[ij] in list_b:
                summ=summ+1
                ij=ij+1
        if summ==pp:
            return True

#========
def findSmallest():
    ppp=1
    while 1:
        if (sd(ppp,ppp*2)==True and sd(ppp,ppp*3)==True and sd(ppp,ppp*4)==True and sd(ppp,ppp*5)==True and sd(ppp,ppp*6)==True):
            return ppp
            break
        else:
            ppp=ppp+1

findSmallest()

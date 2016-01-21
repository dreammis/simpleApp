#-* coding:utf8 -*-
#9*9
for i in range(1,10):
    string = ''+'\t'*(i-1)
    for j in range(i,10):
        string = string+str(i*j)+'\t'
    print string


for i in range(1,10):
    string = ''
    for j in range(1,i+1):
        string = string+str(i*j)+'\t'
    print string+'\t'*(10-i)

'''
find string

A ='ABFABCGABCDM'
B ='ABC'
'''

A ='ABFABCGABCDM'
B ='ABC'
def f_find(str1,str2):
    start = 0
    location = ''
    while True:
        result = A.find(B,start)
        if result != -1:
            location = location+str(result)+'\t'
            start = result+3
        else:
            break
    return location

print f_find(A,B)
'''
no sort()
f_sort()
two parameter
'''
l = [2,4,0,5,8]
def f_sort(li,reverse=False):
    for i in range(len(li)-1,-1,-1):

        for j in range(i):
            if reverse == True:
                if li[j+1]>li[j]:
                    li[j+1],li[j]=li[j],li[j+1]
            else:
                if li[j+1]<li[j]:
                    li[j+1],li[j]=li[j],li[j+1]
    return li
print f_sort(l,True)



'''


	* 有一个列表：[1, 2, 3, 4...n]，n=20；请编写代码打印如下规律的输出：

1 [1*, 2, 3, 4, 5]
2 [1, 2*, 3, 4, 5]
3 [1, 2, 3*, 4, 5]
4 [2, 3, 4*, 5, 6]
5 [3, 4, 5*, 6, 7]
6 [4, 5, 6*, 7, 8]
...

20 [16, 17, 18, 19, 20*]


'''
li = [i for i in xrange(1,100)]

def show(list1):
    for i in list1:
        lis = list1[:]
        l = ''
        if i<=3:
            lis[i-1] = '*'+str(lis[i-1])
            l = str(lis[:5])
            print (str(i)+' '+l).replace('\'','')
        elif i<=len(lis)-3:
            lis[i-1] = '*'+str(lis[i-1])
            l = str(lis[i-3:i+2])
            print (str(i)+' '+l).replace('\'','')
        else:
            lis[i-1] = '*'+str(lis[i-1])
            l = str(lis[len(lis)-5:])
            print (str(i)+' '+l).replace('\'','')
print show(li)


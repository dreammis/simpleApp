#-* coding:utf8 -*-
from xml.etree import ElementTree as xml
import sqlite3
from sys import argv
import time

def openXml(file):
    f = open(file,'r')
    content = f.read()
    content.encode('utf-8')
    content.replace('gb2312','utf-8')
    return content
def analyseUser(content):
    root = xml.fromstring(content)
    userInfo = root.findall(".//Sys_User/")
    userD = []
    for user in userInfo:
        userDic = {}
        userDic['id'] = user.attrib['ID']
        userDic['username'] = user.attrib['UserName']
        userDic['name'] = user.attrib['Name']
        userDic['mobile'] = user.attrib['Mobile']
        userDic['email'] = user.attrib['Email']
        userDic['phone'] = user.attrib['Phone']
        userDic['gender'] = int(user.attrib['Gender'])+1
        userD.append(userDic)
    return userD

def analyseDep(content,userD):
    root = xml.fromstring(content)
    DeptPosition = root.findall('.//RTX_UserDetail/')
    DeptUser = root.findall('.//RTX_DeptUser/')

    for positon in DeptPosition:
        id = positon.attrib['ID']
        for items in userD:
            if id == items['id']:
                items['Position'] = positon.attrib['Position']

    for deptUser in DeptUser:
        id = deptUser.attrib['UserID']
        for items in userD:
            if id == items['id']:
                    items['DeptID'] = deptUser.attrib['DeptID']
    return userD


def analyseRootDep(content,conn):
    root = xml.fromstring(content)
    DeptPosition = root.findall('.//RTX_Dept/')

    cursor = conn.cursor()
    cursor.execute('drop table if exists deptinfo')
    cursor.execute("create table deptinfo(DeptID varchar(20) primary key, PDeptID  varchar(20),DeptName varchar(50))")

    # wholeDeptDic= []
    for singleDept in DeptPosition:
        # deptDic = {}
        # deptDic['DeptID'] = singleDept.attrib['DeptID']
        # deptDic['PDeptID'] = singleDept.attrib['PDeptID']
        # deptDic['DeptName'] = singleDept.attrib['DeptName']
        # wholeDeptDic.append(deptDic)
        cursor.execute("insert into deptinfo (DeptID,PDeptID,DeptName) values (?,?,?)",
                       (singleDept.attrib['DeptID'],singleDept.attrib['PDeptID'],singleDept.attrib['DeptName']))
    conn.commit()

def findDepName(userD):

    for userInfo in userD:
        name = ""
        userDeptId = userInfo['DeptID']
        if userDeptId == '10':
            print (userDeptId)
        name = name +gets(userDeptId,name)
        userInfo['DeptName'] = danweiId + '/'+name.rstrip('/')
    return userD


def gets(userDeptId,name):
    cursor = conn.cursor()
    #当userDeptId是两位数就会提示传入两个参数，这里需要传入元组（x,)
    cursor.execute("select DeptID,PDeptID,DeptName from deptinfo where DeptID=?",(userDeptId,))
    result = cursor.fetchall()
    if result:
        depName = result[0][2]

        pdepId = result[0][1]

        name = depName+'/'+name
        cursor.close()
        if pdepId != '0':
            return gets(pdepId,name)
        else:
            return name


        # reDic = copy.copy(wholeDeptDic)
        #
        #
        #
        # for deptInfo in wholeDeptDic:
        #     name = ''
        #     if userDeptId == deptInfo['DeptID']:
        #         # name = deptInfo['DeptName']+'/'+name
        #         reDic.remove(deptInfo)
        #         getDeptName(deptInfo,reDic,name)

def getDeptName(deptInfo,reDic,name):

    name = deptInfo['DeptName']+'/'+name
    flag = False
    if deptInfo['PDeptID'] !='0':
        for items in reDic:
            if items['DeptID'] == deptInfo['PDeptID']:
                # name = items['DeptName']+'/'+name
                reDic.remove(items)
                getDeptName(items,reDic,name)
    else:
        return name


def outExcel(userD):
    import xlwt
    wbk  = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)

    for index in range(len(userD)):
        sheet.write(index,0,userD[index].get('DeptName'))
        sheet.write(index,1,userD[index]['username'])
        sheet.write(index,2,userD[index]['name'])
        sheet.write(index,3,userD[index]['gender'])
        sheet.write(index,4,userD[index]['email'])
        sheet.write(index,5,userD[index]['mobile'])
        sheet.write(index,6,userD[index]['Position'])
        sheet.write(index,7,'202cb962ac59075b964b07152d234b70')
        sheet.write(index,8,'1')
    wbk.save('antUserInfo.xls')

if __name__ == '__main__':
    utTime = time.time()
    dbfile = 'dept'+str(utTime)+'.db'
    conn = sqlite3.connect(dbfile)
    xmlContent = openXml('rtx.xml')
    danweiId = ''
    if len(argv)>1:
        danweiId = danweiId+argv[1]
        print (danweiId)

    userInfo_1 = analyseUser(xmlContent)
    userInfo_2 = analyseDep(xmlContent,userInfo_1)

    analyseRootDep(xmlContent,conn)
    userInfo_3 = findDepName(userInfo_2)

    print (userInfo_3)
    outExcel(userInfo_3)


    import codecs
    import os
    if os.path.exists('antUserInfo.txt'):
        os.remove('antUserInfo.txt')
    with codecs.open('antUserInfo.txt','a','utf-8') as f:
        for index in range(len(userInfo_3)):
            f.write(str(userInfo_3[index].get('DeptName'))+'\t')
            f.write(str(userInfo_3[index]['username'])+'\t')
            f.write(str(userInfo_3[index]['name'])+'\t')
            f.write(str(userInfo_3[index]['gender'])+'\t')
            f.write(str(userInfo_3[index]['email'])+'\t')
            f.write(str(userInfo_3[index]['mobile'])+'\t')
            f.write(str(userInfo_3[index]['Position'])+'\t')
            f.write('202cb962ac59075b964b07152d234b70'+'\t')
            f.write('1'+'\r\n')
    conn.close()

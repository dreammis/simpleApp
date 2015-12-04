#-* coding:utf8 -*-
from xml.etree import ElementTree as xml

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

def analyseRootDep(content,userD):
    root = xml.fromstring(content)
    DeptPosition = root.findall('.//RTX_Dept/')

    for dept in DeptPosition:
        deptId = dept.attrib['DeptID']
        for items in userD:
            if deptId == items['DeptID']:
                    items['DeptName'] = dept.attrib['DeptName']

    return userD

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
    wbk.save('ant.xls')

if __name__ == '__main__':
    xmlContent = openXml('rtx.xml')

    userInfo_1 = analyseUser(xmlContent)
    userInfo_2 = analyseDep(xmlContent,userInfo_1)
    userInfo_3 = analyseRootDep(xmlContent,userInfo_2)
    print (userInfo_3)
    outExcel(userInfo_3)
    with open('rm.txt','w+') as f:
        for items in userInfo_3:
            f.write(str(items)+'\n')

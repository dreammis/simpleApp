#-* coding:utf8 -*-
import pandas as pd
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_userInfo(user_dict):

    userList = pd.read_excel('GetListUser.xls',encoding="gb2312")
    # deptList = pd.read_excel('GetListDept.xls',encoding="gb2312")
    # user_dept_list = pd.read_excel('GetListUserDept.xls',encoding="gb2312")
    for index in xrange(len(userList)):
        user_info = {}
        user_info['USERCODE'] = userList.USERCODE[index]
        user_info['USERNAME'] = userList.USERNAME[index]
        user_info['USERPWD'] = '202cb962ac59075b964b07152d234b70'
        user_info['SEX'] = userList.SEX[index]
        user_info['EMAIL'] = userList.EMAIL[index]
        user_info['LONGMOBILE'] = userList.LONGMOBILE[index]
        user_info['OFFICEPHONE'] = userList.OFFICEPHONE[index]
        user_info['POST1'] = userList.POST1[index]
        user_info['DPTCODE'] = userList.DPTCODE[index]
        user_dict.append(user_info)
    return user_dict

def getdept(user_dict):

    deptList = pd.read_excel('GetListDept.xls',encoding="gb2312")
    depttem = []
    for userinfo in user_dict:
        deptname = '/'
        try:
            dptcode = deptList[deptList.DPTCODE==userinfo['DPTCODE']].DPTCODE.values[0]
        except Exception:
            userinfo['DPTNAME'] = ''
            continue
        deptname = getDept(dptcode,deptList,deptname)
        userinfo['DPTNAME'] = deptname
    return user_dict



def getDept(dptcode,deptList,name):
    dptcodeP = deptList[deptList.DPTCODE==dptcode].PDPTCODE.values[0]
    name = deptList[deptList.DPTCODE==dptcode].DPTNAME.values[0]+'/'+name
    if dptcodeP!=-1:
        return getDept(dptcodeP,deptList,name)
    else:
        return name


if __name__ == '__main__':
    user_dict = []
    get_userInfo(user_dict)
    # t = threading.Thread(target=getdept,name='getdeptThread',args=user_dict)
    # t.start()
    # t.join()
    user_dict = getdept(user_dict)
    import codecs
    import os
    filepath = os.path.curdir
    if os.path.exists(os.path.join(filepath,'antUserInfo.txt')):
        os.remove(os.path.join(filepath,'antUserInfo.txt'))
    with codecs.open(os.path.join(filepath,'antUserInfo.txt'),'a','utf-8') as f:
        for index in xrange(len(user_dict)):
            f.write(str(user_dict[index].get('DPTNAME'))+'\t')
            f.write(str(user_dict[index]['USERCODE'])+'\t')
            f.write(str(user_dict[index]['USERNAME'])+'\t')
            f.write(str(user_dict[index]['SEX'])+'\t')
            f.write(str(user_dict[index]['EMAIL'])+'\t')
            f.write(str(user_dict[index]['LONGMOBILE'])+'\t')
            f.write(str(user_dict[index]['POST1'])+'\t')
            f.write('202cb962ac59075b964b07152d234b70'+'\t')
            f.write('1'+'\r\n')
#-* coding:utf8 -*-

'''
首先使用索引，提升了效率。
其次程序端校验
使用union
文件夹中是windows 下 mysql和python的连接驱动 x86&x64
'''
from __future__ import print_function
import torndb
import time
import random

def get_mysql_conn():
    return torndb.Connection(
        host=mysql["host"]+":"+mysql["port"],
        database=mysql["database"],
        user=mysql["user"],
        password=mysql["password"],
        charset="utf8"
    )

mysql = {
    "host":"localhost",
    "port":"3306",
    "database":"greps_list",
    "password":"123456",
    "user":"root",
    "charset":"utf-8"
}

def ip2int(ip):
    try:
        hexn = ''.join(["%02X" % long(i) for i in ip.split('.')])
    except Exception, e:
        hexn = ''.join(["%02X" % long(i) for i in '0.0.0.0'.split('.')])
    return long(hexn, 16)


def int2ip(n):
    d = 256 * 256 * 256
    q = []
    while d > 0:
        m,n = divmod(n,d)
        q.append(str(m))
        d = d/256
    return '.'.join(q)

def insert_row():
    with open("ipdata.csv","r") as f:
        lines = f.readlines()
    nl_p_list = []
    for l in lines:
        ls = l.strip().split(',', 4)
        c1, c2, c3, c4, c5 = ls[0], ip2int(ls[1]), ip2int(ls[2]), ls[3], ls[4]
        nl = [c2, c3, c4, c5]
        nl_p_list.append(nl)
    t1 = time.time()
    db = get_mysql_conn()
    db.execute("START TRANSACTION")
    for i in range(len(nl_p_list)/1000 + 1):
        tmp_nl_p_list = nl_p_list[i*1000: (i+1)*1000]
        ret = db.insertmany('insert into ipdata (startip, endip, country, carrier) values (%s, %s, %s, %s)', tmp_nl_p_list)
        print ("1000 has done;")
    db.execute("COMMIT")

if __name__=="__main__":
    with open("ipdata.csv","r") as f:
        lines = f.readlines()
    nl_p_list = []
    for l in lines:
        ls = l.strip().split(',', 4)
        c1, c2, c3, c4, c5 = ls[0], ip2int(ls[1]), ip2int(ls[2]), ls[3], ls[4]
        nl = [c2, c3, c4, c5]
        nl_p_list.append(nl)
    db = get_mysql_conn()
    ip_list = map(lambda x:x[1],random.sample(nl_p_list,100))

    sql_tmp = "select {0}.* from(select * from ipdata where %s>=startip order by startip DESC limit 1){0}"
    sql_list = []
    for i in range(len(ip_list)):
        sql_list.append(sql_tmp.format('t'+str(i))%ip_list[i])
    sql = " union all ".join(sql_list)
    t0 = time.time()
    dict(zip(ip_list,db.query(sql)))
    t1= time.time()
    print (t1-t0)

    retList = []
    for ip in ip_list:
        ret = db.get('select * from ipdata where %s>=startip order by startip DESC  limit 1'%ip)
        startip,endip = ret.get("startip"),ret.get("endip")
        if startip<=ip<=endip:
            retList.append(ip)
        else:
            retList.append(ip,"unknown")
    t2 = time.time()
    print (t2-t1)


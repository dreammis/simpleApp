#-* coding:utf8 -*-
#Int To Ip
def IntToDottedIP( intip ):
    octet = ''
    for exp in [3,2,1,0]:
        octet = octet + str(intip / ( 256 ** exp )) + "."
        intip = intip % ( 256 ** exp )
    return(octet.rstrip('.'))

#IP To INT
def DottedIPToInt( dotted_ip ):
    exp = 3
    intip = 0
    for quad in dotted_ip.split('.'):
        intip = intip + (int(quad) * (256 ** exp))
        exp = exp - 1
    return(intip)


s = '192.168.1.1'
print DottedIPToInt(s)

print IntToDottedIP(3232235777)
'''
还有一种方法，我只试验过mysql。
select inet_aton('192.168.1.1')
+--------------------------+
| inet_aton('192.168.1.1') |
+--------------------------+
|               3232235777 |
+--------------------------+
1 row in set (0.07 sec)


select inet_ntoa('3232235777')
+-------------------------+
| inet_ntoa('3232235777') |
+-------------------------+
| 192.168.1.1             |
+-------------------------+
1 row in set (0.00 sec)

'''
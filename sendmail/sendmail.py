#-* coding:utf8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.getcwd(),'myConfig.ini'))
sender = config.get('senderinfo','sender')
username = config.get('senderinfo','username')
password = config.get('senderinfo','pwd')
receiver = config.get('receiverinfo','receiver')

subject = 'python email test'
smtpserver = 'smtp.sina.com'

msg = MIMEText(u'''
<h1>this is a html email</h1>
<a href="gmail.com" title="这是我的新邮箱" target="_blank">这是我的新邮箱</a>
'''
               ,'html','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
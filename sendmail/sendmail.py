#-* coding:utf8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
import ConfigParser
import os

#send mail with a image


config = ConfigParser.ConfigParser()
config.read(os.path.join(os.getcwd(),'myConfig.ini'))
sender = config.get('senderinfo','sender')
username = config.get('senderinfo','username')
password = config.get('senderinfo','pwd')
receiver = config.get('receiverinfo','receiver')

subject = 'python email test'
smtpserver = 'smtp.sina.com'



msgRoot = MIMEMultipart('relate')
msgRoot['Subject'] = 'test message'
msgText = MIMEText('''<b> Some <i> HTML </i> text </b > and an image.
<img alt="" src="cid:image1"/>good!''',
                   'html', 'utf-8')
msgRoot.attach(msgText)

with open('1%2Fwallpages%2F201507%2Fjuly2-1440x900.jpg','rb') as f:
    msgImage = MIMEImage(f.read())

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)


smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
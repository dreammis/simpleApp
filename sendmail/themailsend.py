import ConfigParser
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import os

# To finish the mail without the people jiaohu
class Mail():
    def __init__(self):
        self.sendtype = {
            "1":self.sendNormalText,
            "2":self.sendHtmlText,
            "3":self.sendMailWithImage,
            "4":self.sendMailWithAttach,
            "5":self.sendServeralMail,
            "6":self.sendMixMail,
        }
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.getcwd(),"myconfig.ini"))
        self._mailInfo = self.getMailInfoFromConfig(config)
        self.subject = "This is The Lyu Test"

    def getMailInfoFromConfig(self,configEd):
        mailInfo = {}
        mailInfo['sender'] = configEd.get('senderinfo','sender')
        mailInfo['receiver'] = configEd.get('receiverinfo','receiver')
        mailInfo['password'] = configEd.get('senderinfo','pwd')
        mailInfo['mailServer'] = configEd.get('mailConfig','host')
        return mailInfo

    def sendNormalText(self):
        msg = MIMEText('This is'+str(datetime.now())+'from my app send','plain','utf-8')
        msg['Subject'] = Header(self.subject,'utf-8')
        self.sendMail(msg)

    def sendHtmlText(self):
        msg = MIMEText(u"""
        <h1>This is my own mail to Test the Python's Mail method.</h1>
        """,'html','utf-8')
        msg['Subject'] = Header(self.subject,'utf-8')
        self.sendMail(msg)
    def sendMailWithImage(self):
        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = self.subject
        msgText = MIMEText("""
        <h1>This mail contains a pic of wow</h1>
        <img alt="" src="cid:image1"/>
        good!
        """,'html','utf-8')
        msgRoot.attach(msgText)
        with open('1%2Fwallpages%2F201507%2Fjuly2-1440x900.jpg','rb') as f:
            msgImage = MIMEImage(f.read())
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        self.sendMail(msgRoot)


    def sendMailWithAttach(self):
        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = self.subject
        attachItems = MIMEText(open('Detial.txt','rb').read(),_subtype='base64',_charset='utf-8')
        attachItems['Content-Type'] = 'application/octet-stream'
        attachItems["Content-Disposition"] = 'attachment; filename="Detial.txt"'
        msgRoot.attach(attachItems)

        self.sendMail(msgRoot)

    def sendServeralMail(self):
        'The only due to send serveral Mail is to give the function of sendmail() a list.'
        #senderList=['xx@xx.com','oo@oo.com']
        msg = MIMEText('This mail sended to lots of persons.Not only you',_subtype='plain',_charset='utf-8')
        msg['Subject'] = Header(self.subject + " and it sended to lots of Person",'utf-8')
        self.sendMail(msg)

    def sendMixMail(self):
        msgRoot = MIMEMultipart('Mixed')
        msgRoot['Subject'] = Header(self.subject+' wow!, This mail contains lots of staff!!','utf-8')
        msgText = 'Hi,I\'m a mixed staff mail,will you love me ?'
        msgHtml = '''
        <h1>
        How Are You Today.
        Here is the <a href="http://www.python.org">link</a> you wanted.
        </h1>
        '''
        part1 = MIMEText(msgText,'plain')
        part2 = MIMEText(msgHtml,'html')

        attachItems = MIMEText(open('Detial.txt','rb').read(),'base64','utf-8')
        attachItems['Content-Type'] = 'application/octet-stream'
        attachItems["Content-Disposition"] = 'attachment; filename="Detial.txt"'

        msgRoot.attach(part1)
        msgRoot.attach(part2)
        msgRoot.attach(attachItems)
        msgRoot['Reply-to'] = '10010@qq.com'
        msgRoot['From']="God<firedirx@sina.com>"
        self.sendMail(msgRoot)

    def sendMail(self,msg):
        smtp = smtplib.SMTP()
        mailServer = self._mailInfo.get('mailServer')

        sender = self._mailInfo.get('sender')
        pwd = self._mailInfo.get('password')
        receiver = self._mailInfo.get('receiver')
        smtp.connect(mailServer)
        smtp.login(sender,pwd)
        smtp.sendmail(sender,receiver,msg.as_string())
        print "[*]Mail Send Success!"
        smtp.quit()


#todo get all the file in dirs including the inner ones;
def GetFileList(dir, fileList=[]):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #if want to remove some fonlder
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList



if __name__ == '__main__':
    mail = Mail()
    mail.sendMixMail()
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
  
def hello():
    print('hello world')
    
def mail(topic = '数据统计邮件',
         formatText = '',
         fileNameList = [],
         my_user = 'fleebt@163.com', 
         my_sender = 'Info_Flee@163.com', 
         my_pass = '930630flee'):
    ret=True
    try:
        msg = MIMEMultipart()

        #msg=MIMEText('本邮件为系统自动发送，请勿回复\n使用中遇到问题，请联系fleebt@163.com','plain','utf-8')
        msg['From']=formataddr(["Admin",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["Flee",my_user])       # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']= topic                        # 邮件的主题，也可以说是标题
        msg.attach(MIMEText(formatText + '\n\n本邮件为系统自动发送，请勿回复\n使用中遇到问题，请联系fleebt@163.com', 'plain', 'utf-8'))

        # 构造附件，传送当前目录下的文件
        if not fileNameList:
            for fileName in fileNameList:
                att = MIMEText(open(fileName, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
                att["Content-Disposition"] = 'attachment; filename="' + fileName + '"'
                msg.attach(att)
        server=smtplib.SMTP_SSL("smtp.163.com", 994)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
        print(e)
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
    return ret
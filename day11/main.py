
'''
    入口程序：
        用于扫描加法，减法用例
        并执行得到测试报告
    1.HTMLTestRunner

'''
from HTMLTestRunner import HTMLTestRunner
import unittest

# 加载16条用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\12036\PycharmProjects\pythonProject\python\day11",pattern="Test*.py")

# 创建运行器，来运行16条用例
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description="加减乘除的测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="w+",encoding="utf-8")
)


# 生成测试报告
runner.run(tests)



import smtplib  # 加载smtplib模块
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class Send_Email():

    def send_email(self, report_path):
        """
            to_list:发给谁
            sub:主题
            content:内容
            send_mail("aaa@126.com","sub","content")
        """
        '''第三方
        SMTP
        服务'''
        mail_host = 'smtp.qq.com'  # 设置服务器
        mail_port = 25  # 25 为 SMTP 端口号
        to_list = ['1203687250@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        mail_user = '1203687250@qq.com'  # 用户名
        mail_pass = 'kpfsibmsrnxtigjb'  # 密码

        with open(report_path, 'rb') as file:
            mail_body = file.read()
            me = "1203687250@qq.com"
            text = MIMEText(mail_body, 'html', 'utf-8')
            # 创建一个带附件的实例
            msg = MIMEMultipart('mixed')
            # ‘’‘三个参数：第一个为文本内容，第二个
            # plain
            # 设置文本格式，第三个
            # utf - 8
            # 设置编码
            msg.attach(MIMEText('Hi，all！附件是接口自动化测试报告，请查收，自动发送，无需回复~', 'plain', 'utf-8'))
            text.add_header("Content-Disposition", "attachment", filename=("gbk", "", "接口自动化测试报告.html"))
            msg.attach(text)

        msg['Subject'] = u'接口自动化测试报告'  # 邮件的主题，也可以说是标题
        msg['From'] = me  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = ";".join(to_list)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        try:
            s = smtplib.SMTP(mail_host, mail_port)  # 发件人邮箱中的SMTP服务器，端口
            s.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            s.sendmail(me, to_list, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            s.close()  # 关闭连接
            print("邮件发送成功", to_list)
            return True
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print(e)
            return False


Send_Email().send_email('计算器.html')
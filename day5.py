import random

# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"


def welcome():
    print("---------------------------------------")
    print("-     中国工商银行账户管理系统V1.0         -")
    print("---------------------------------------")
    print("-  1.开户                              -")
    print("-  2.存钱                              -")
    print("-  3.取钱                              -")
    print("-  4.转账                              -")
    print("-  5.查询                              -")
    print("-  6.Bye!                             -")
    print("---------------------------------------")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, door, money):
    if len(bank) > 100:
        return 3
    if username in bank:
        return 2
    # 正常开户
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 开户的输入数据
def addUser():
    username = input("请输入姓名：")
    password = input("请输入密码：")
    country = input("请输入国籍：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入您家门牌号：")
    money = int(input("请输入初始化您的银行卡余额："))
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, door, money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s 元
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username, account, password, country, province, street, door, money, bank_name))
        print(bank)


# 存钱
def bank_cunmoney():
    username = input("请输入用户名:")
    addmoney = int(input("请输入存款金额:"))
    add = add_money(username, addmoney)
    if add == 1:
        print("存钱成功")
        print("下面是您的账户信息:")
        info = '''
            --------------账户信息--------------
            用户名：%s
            存款金额: %s 元
            账户余额: %s 元
            ----------------------------------
            '''
        print(info % (username, addmoney, bank[username]['money']))
    elif add == False:
        print("用户不存在")


def add_money(username, addmoney):
    if username in bank:
        bank[username]['money'] = bank[username]['money'] + addmoney
        return 1
    else:
        return False


# 取钱
def bank_qumoney():
    username = input("请输入用户名:")
    password = input("请输入密码：")
    addmoney = int(input("请输入取款金额:"))
    add = add_qumoney(username, password, addmoney)
    if add == 3:
        print("余额不足")
    elif add == 2:
        print("密码不正确")
    elif add == 1:
        print("用户不存在")
    elif add == 0:
        print("取钱成功")
        print("下面是您的账户信息:")
        info = '''
            --------------账户信息--------------
            用户名：%s
            取款金额: %s 元
            账户余额: %s 元
            ----------------------------------
            '''
        print(info % (username, addmoney, bank[username]['money']))


def add_qumoney(username, password, addmoney):
    if username not in bank:
        return 1
    if bank[username]['password'] != password:
        return 2
    bank[username]['money'] = bank[username]['money'] - addmoney
    if bank[username]['money'] < 0:
        return 3
    else:
        return 0
# 转账
def transfer():
    username = input("请输入转出账户用户名:")
    account = input("请输入转出账户账号:")
    password = input("请输入转出账户密码：")
    username1 = input("请输入转入账户用户名:")
    account1 = input("请输入转入账户账号:")
    money = input("请输入转账金额:")
    transfer = transfer_process(username, account, password, username1, account1, money)
    if transfer == 1:
        print("账号输入错误")
    elif transfer == 2:
        print("密码输入错误")
    elif transfer == 3:
        print("余额不足")
    else:
        print("转账成功，下面是您的转账信息:")
        info = '''
        --------------转账信息--------------
        转出账户用户名: %s
        转出账户账号: %s
        转入账户用户名: %s
        转入账户账号: %s
        转 账 金 额: %s 元
        账 户 余 额: %s 元
        ----------------------------------
        '''
        print(info % (username, account, username1, account1, money, bank[username]['money']))
# 处理转账
def transfer_process(username,account,password,username1,account1,money):
    if username in bank and username1 in bank:
        if password == bank[username]['password']:
            if float(money) <= bank[username]['money']:
                bank[username] = {
                    "account": bank[username]["account"],
                    "password": bank[username]["password"],
                    "country": bank[username]["country"],
                    "province": bank[username]["province"],
                    "street": bank[username]["street"],
                    "door": bank[username]["door"],
                    "money": bank[username]['money'] - float(money),
                    "bank_name": bank_name
                }
                bank[username1] = {
                    "account": bank[username1]["account"],
                    "password": bank[username1]["password"],
                    "country": bank[username1]["country"],
                    "province": bank[username1]["province"],
                    "street": bank[username1]["street"],
                    "door": bank[username1]["door"],
                    "money": bank[username1]['money'] + float(money),
                    "bank_name": bank_name
                }
            else:
                return 3
        else:
            return 2
    else:
        return 1

# 查询
def query():
    username = input("请输入用户名:")
    account = input("请输入账号:")
    password = input("请输入密码：")
    if username in bank:
        if password == bank[username]['password']:
            info = '''
            ------------当前账户信息------------
            账   号: %s
            密   码: ******
            余   额: %s 元
            居住地址: %s
            开 户 行: %s
            ----------------------------------
            '''
            print(info % (account, bank[username]['money'], bank[username]['country']+bank[username]['province']+bank[username]['street']+bank[username]['door'], bank[username]['bank_name']))
        else:
            print("密码输入错误")
    else:
        print("该用户不存在")

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        bank_cunmoney()
    elif chose == "3":
        bank_qumoney()
    elif chose == "4":
        transfer()
    elif chose == '5':
        query()
    elif chose == '6':
        print("bye~")
        exit()
    else:
        print("输入错误")



import random
Ran = random.randint(0, 150)
i = 0
m = 5000
while i < 10:
    num = input("请输入一个数字")
    num = int(num)
    i = i + 1
    if num == Ran:
        print("恭喜你，猜中，本次猜的数字为", num)
        i = i + 10
        m = m + 3000
    elif num < Ran:
        print("小了")
        m = m - 500
    else:
        print("大了")
        m = m - 500
if m == 0:
    print("你的金币已空")
else:
    print("你的金币为", m)

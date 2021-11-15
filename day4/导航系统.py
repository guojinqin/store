
'''
    导航系统：
        1.字典数据。
        2.方法的使用。

        1.退出：输入q或者Q
任务1：
    将旅游导航系统结合商城系统，集成开发！
    需求：
        当最终到达景点后，询问是否去买纪念品？
            xxxxXXXXxxxxxxxxxxx
'''

citys = {
    "北京":{
        "昌平":{
            "十三陵":["十三陵水库"],
            "八达岭":["八达岭长城","野生动物园"],
            "回龙观":["五道口切糕","甑糕","呷哺呷哺","海底捞"]
        },
        "海淀":{
            "高校":["清华","北大"],
            "景点":["香山","植物园"]
        },
        "朝阳":{
            "公园":["玉渊潭公园","朝阳南北塔"]
        },
        "延庆":{
            "景点":["龙庆峡"]
        }
    },
    "上海":{
        "浦东新区":{
            "叶榭市":["外滩公园","外滩"]
        }
    }
}

def showCity(citys):
    print("---------欢迎来到旅游导航系统！-------------")
    for i in citys:
        print(i)
    print("---------------------------------------")


#
while True:
    showCity(citys)
    chose = input("请输入您想去的一级城市：")
    if chose == 'q' or chose == 'Q':
        print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
        break  # 跳出循环
    if chose not in citys:
        print("温馨提示：当前城市没有项目！别瞎弄！")
    else:
        showCity(citys[chose])
        chose2 = input("请输入您想去的二级城市：")
        if chose2 == 'q' or chose2 == 'Q':
            print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
            break  # 跳出循环
        if chose2 not in citys[chose]:
            print("都跟你讲了没有这个城市项目，别瞎弄！")
        else:
            showCity(citys[chose][chose2])
            chose3 = input("请输入您想去的三级城市：")
            if chose3 == 'q' or chose3 == 'Q':
                print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
                break  # 跳出循环
            if chose3 not in citys[chose][chose2]:
                print("你故意找茬是不是？别瞎弄！")
            else:
                showCity(citys[chose][chose2][chose3])
                print("车已经达到！祝你玩的愉快！")
                shop = input('是否需要购物？(请输入yes or no)')
                if shop == 'yes' or shop == 'Yes':
                    import 购物
                else:
                    print("祝你玩的愉快！")
















































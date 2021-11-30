# 杯子
class cup:
    hight = ""
    volume = ""
    color = ""
    material = ""
    name = ""


    def drink(self):
        print(self.name,"的杯子在天上")

    def showMe(self):
        print("一个叫",self.name,"的",self.material,"材质的",self.color,"的杯子装了",self.volume,"L水在天上飞")

c = cup()
c.color = "五彩斑斓的黑"
c.volume = 5
c.hight = "10"
c.material = "钛合金"
c.name = "神"

c.drink()
c.showMe()
#----------------------------------------------------------------------------------------------------------------
#电脑
class computer:
    size = ""
    money = ""
    cpu = ""
    memory = ""
    time = ""
    brand = ""

    def typing(self):
        print(self.brand,"电脑可以进行长时间打字")
    def paly(self):
        print(self.brand,"可以稳定运行LOL、PUBG以及各种3A大作")
    def see(self):
        print(self.brand,"看视频毫无压力")
    def showMe(self):
        print("一台", self.brand, "电脑在", self.time, "的时间里用", self.size, "英寸的屏幕一边放视频一边游戏打字展示素质")
co = computer()
co.brand = "外星人"
co.time = "无穷尽"
co.cpu = "i9 11900K"
co.money = "23999"
co.size = "17.2"
co.memory = "2T"

co.typing()
co.paly()
co.see()
co.showMe()
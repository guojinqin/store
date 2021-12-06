from unittest import TestCase
from  Calc import Calc

# 只是测试用例
class TestCalc(TestCase):

    def testMinus1(self):
        # 造数据
        a = -6
        b = 5
        s = -30  # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        multi = calc.multi(a, b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s, multi)

    def testMinus2(self):
        # 造数据
        a = -6
        b = -5
        s = 30  # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        multi = calc.multi(a, b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s, multi)
    def testMinus3(self):
        # 造数据
        a = 6
        b = -5
        s = -30  # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        multi = calc.multi(a, b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s, multi)
    def testMinus4(self):
        # 造数据
        a = 6
        b = 5
        s = 30   # 期望结果

        # 调用加法方法，得到实际结果
        calc = Calc()
        multi = calc.multi(a, b)

        # 判断实际结果与期望结果是否一致。
        self.assertEqual(s, multi)

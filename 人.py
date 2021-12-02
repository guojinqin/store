class person:
    name = ''
    age = 0
    gender = ''

class worker(person):
    def work(self,tyen):
        print(self.name,'正在',tyen)
class student(person):
    def study():
        print('正在学习')
    def sing():
        print('正在唱歌')


p = person()

p.name = '刘宇名'
p.age = 154
p.gender = '女'

w = worker()
w.work('干活')

s = student()
s.study()










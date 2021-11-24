import xlrd

# 工作簿对象
wb = xlrd.open_workbook(filename=r"D:\Ceshikaifa\python任务\百度合作单位-人员管理-二期.xls")

st = wb.sheet_by_index(0)

rows = st.nrows
cols = st.ncols

# 总薪资，和平均年龄
# sum_age = 0
# sum_sal = 0
a = 0 #男
b = 0 #女
c = 0 #大于45
d = 0 #薪资大于8000
e = 0 #小于3000
f = 0 #电信14、17
g = 0 #移动13
h = 0 #联通15
i = 0 #传媒
k = 0 #风险（黑，北京，福建，四川）
for j in range(1,rows):
    data = st.row_values(j)
    if data[8] == "男":
        a = a+1
    elif data[8] == "女":
        b = b+1
    if data[7] >45:
        c = c+1
    if data[11] > 8000:
        d = d+1
    elif data[11] < 3000:
        e = e+1
    if data[5].startswith("14") or data[5].startswith("17"):
        f = f+1
    elif data[5].startswith("13"):
        g = g+1
    elif data[5].startswith("15"):
        h = h+1
    if data[13].endswith("传媒有限公司"):
        i =i+1
    if data[9].startswith("黑龙江") or data[9].startswith("北京") or data[9].startswith("福建") or data[9].startswith("四川"):
        k =k+1
    # sum_age = sum_age + data[1]
    # sum_sal = sum_sal + data[2]
print("总公司男生人数为：",a,"女生人数为：",b)
print("年龄大于45的人数：",c)
print("薪资大于8000：",d,"薪资小于3000",e)
print("电信：",f,"移动：",g,"联通：",h)
print("传媒公司人数：",i)
print("风险地区人数：",k)
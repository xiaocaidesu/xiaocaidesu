from pyecharts.charts import Bar
import xlrd  #xlrd  xlwt 读 写 模块 pip install + 模块名添加

data = xlrd.open_workbook('舰b统计.xlsx')

# print(data)  #查看地址

table = data.sheets()[4]

#print(table.nrows) #获取这张表有多少行
#print(table.ncols) #获取这张表有多少列
#print(table.row_values(0)) #获取数据

names = []
sales = []

for i in range (0,table.nrows ):
    name = table.row_values(i)[1]
    names.append(name)
    sale = table.row_values(i)[3]
    sales.append(sale)
#print (names)

# 柱状图
bar = Bar()
bar.add_xaxis(names)
bar.add_yaxis('cv',sales)
bar.render('cv.html')


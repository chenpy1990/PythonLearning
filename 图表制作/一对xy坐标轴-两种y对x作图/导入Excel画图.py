import pandas as pd  # 用于导入Excel的库，处理DataFrame数据
import matplotlib.pyplot as plt  # 用于绘图的库
from matplotlib import rcParams # 用于显示中文  
import numpy as np  # 用于调整网格密度，如果y和x有数学计算关系，也可用

# 设置字体
rcParams['font.sans-serif'] = 'SimHei'  
# 读取Excel文件  
data_path = '一对xy坐标轴-两种y对x作图\出生率和死亡率随年份的变化.xlsx'  # 替换为你的Excel文件路径  
df = pd.read_excel(data_path, engine='openpyxl')  # 读取数据到DataFrame  
  
# 假设你的数据在'x_column'和'y_column'列中  
# 将这些列分别赋值给x和y  
x = df['年份']  # 替换'x_column'为你的x数据所在列的名字 ，X轴 
y1 = df['出生率']  # 替换'y_column'为你的y数据所在列的名字，第一天曲线 
y2 = df['死亡率']  # 这是另外一条曲线
  
# 创建一个图形  
plt.figure(figsize=(8, 6))  # 设置图形大小 

# 绘制数据  
plt.plot(x, y1, label='出生率', marker='o')  # marker表示标记种类
plt.plot(x, y2, label='死亡率', marker='*')

# 添加标题和标签  
plt.title('出生率和死亡率随年份的变化关系')
plt.xlabel('年份')  
plt.ylabel('比率')  
plt.legend()  # 显示图例，如果没有标签，可以删去

# 设置更密集的刻度  
plt.xticks(np.arange(min(x), max(x), 5))  # x轴每隔5设置一个刻度  
plt.yticks(np.arange(5, 25, 1))  # y轴每隔1设置一个刻度   
# 显示网格  
plt.grid(True)  # 网格线密度可以通过调整刻度尺寸调节
  
# 保存图形为图片文件，支持多种格式，如PNG, JPEG, SVG, PDF, EPS等  
plt.savefig('出生率和死亡率随年份的变化关系.png')  # 将图片保存为PNG格式，位置在上一层  
  
# 显示图形（在Jupyter Notebook等环境中）  
plt.show()  

import pandas as pd  # 导入Excel，处理DataFrame数据
import matplotlib.pyplot as plt  # 用于绘图的库
from matplotlib import rcParams # 显示中文  
import numpy as np  # 用于调整网格密度，如果y和x有数学计算关系，也可用
from matplotlib.ticker import MultipleLocator  # 设置刻度用的

rcParams['font.sans-serif'] = 'SimHei'  # 设置字体
# 读取Excel文件  
data_path = 'twinx方法-两个y轴-两种y对x作图\人口数量和粮食产量随时间的变化.xlsx'  # 替换为你的Excel文件路径  
df = pd.read_excel(data_path, engine='openpyxl')  # 读取数据到DataFrame  
  
# 假设你的数据在'x_column'和'y_column'列中,将这些列分别赋值给x和y   
x = df['年份']  # 替换'x_column'为你的x数据所在列的名字 ，X轴 
y1 = df['人口数量（万）']  # 替换'y_column'为你的y数据所在列的名字，第一条曲线 
y2 = df['粮食产量（万吨）']  # 这是另外一条曲线

fig, ax1 = plt.subplots()  # 创建一个fig和axes对象并设置图像大小
fig.set_size_inches(8, 6)  # 设置图片尺寸


color = 'tab:red'  # 设置图片颜色
ax1.set_xlabel('年份')
ax1.set_ylabel('人口数量（万）', color = color)
ax1.plot(x, y1, label='人口数量（万）', color = color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)  # 修改的是 y 轴刻度标签的颜色

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('粮食产量（万吨）', color = color)
ax2.plot(x, y2, label='粮食产量（万吨）', color = color, marker='*')
ax2.tick_params(axis='y', labelcolor = color)
# 添加标题和标签  
plt.title('人口和粮食产量随年份的变化关系')

# ax1.legend(handles=ax1.get_lines(), loc='upper left')
# ax2.legend(handles=ax2.get_lines(), loc='upper right') 

ax1.legend(loc='upper left', bbox_to_anchor=(0, 0.95))
# 显示第二个图例，稍微低于第一个图例，调整bbox_to_anchor的y值来微调位置
ax2.legend(loc='upper left', bbox_to_anchor=(0, 0.85))
# bbox_to_anchor参数的值是相对于图例框的大小的，根据图表的大小和布局来调整这些值


# 设置X轴的刻度位置，每隔5年一个刻度
x_ticks = [year for year in x[1::5]]  # 从x中选择每隔5个元素，调整到让x轴从1950开始
ax1.set_xticks(x_ticks)
# 设置X轴的刻度标签，旋转45度并向右对齐
ax1.set_xticklabels([str(year) for year in x_ticks], rotation=45, ha='right')
# 设置X轴的主刻度位置
# ax1.set_xticks(x)  # 使用这个画的图太密了
# 设置X轴的刻度标签
# ax1.set_xticklabels([str(year) for year in x], rotation=45, ha='right')

# 为 ax1 的 y 轴设置主刻度和次刻度的间隔
ax1.yaxis.set_major_locator(MultipleLocator(20000))  # 主刻度间隔为 5
ax1.yaxis.set_minor_locator(MultipleLocator(10000))  # 次刻度间隔为 1

# 为 ax2 的 y 轴设置主刻度和次刻度的间隔
ax2.yaxis.set_major_locator(MultipleLocator(10000))  # 主刻度间隔为 50
ax2.yaxis.set_minor_locator(MultipleLocator(5000))  # 次刻度间隔为 10

# 以ax1为准添加网格
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)  
# plt.grid(True)  # 显示网格，网格线密度可以通过调整刻度尺寸调节

fig.tight_layout()  # 调整图形布局使其更美观  
# 保存图形为图片文件，支持多PNG, JPEG, SVG, PDF, EPS等  
plt.savefig('人口和粮食产量随年份的变化关系.png')  # 将图片保存为PNG格式，位置在上一层  
    
plt.show()  

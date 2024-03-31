import matplotlib.pyplot as plt  
# import numpy as np
from matplotlib import rcParams # 用于显示中文  

# 设置字体
rcParams['font.sans-serif'] = 'SimHei'
# 创建一个简单的数据集  
# x = np.linspace(0, 10, 100)  
# y = np.sin(x)  

x = [1, 2, 3, 4, 5, 6]
y = [4, 6, 8, 10, 12, 14]
  
# 创建一个图形  
plt.figure(figsize=(8, 6))  # 设置图形大小  
  
# 绘制数据  
# plt.plot(x, y, label='y随x的变化关系')  
# 不想显示标签可以舍去，因为只有一条曲线
plt.plot(x, y, label= None)  

  
# 添加标题和标签  
plt.title('y随x的变化关系')  
plt.xlabel('xxxxx')  
plt.ylabel('yyyyyyy')  
# plt.legend()  # 显示图例，如果没有标签，可以删去
  
# 显示网格  
plt.grid(True)  
  
# 保存图形为图片文件，支持多种格式，如PNG, JPEG, SVG, PDF, EPS等  
plt.savefig('y随x的变化关系.png')  # 将图片保存为PNG格式  
  
# 显示图形（在Jupyter Notebook等环境中）  
plt.show()
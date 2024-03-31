import matplotlib.pyplot as plt  
# import numpy as np # 如果没有涉及到y对x的计算可以舍去
from matplotlib import rcParams # 用于显示中文  

# 设置字体
rcParams['font.sans-serif'] = 'SimHei'
# 创建一个简单的数据集  
# x = np.linspace(0, 10, 100)  
# y = np.sin(x)  

x = [1, 2, 3, 4, 5, 6]
y1 = [2, 4, 6, 8, 10, 12]
y2 = [3, 6, 9, 12, 15, 18]
  
# 创建一个图形  
plt.figure(figsize=(8, 6))  # 设置图形大小  
  
# 绘制数据  
plt.plot(x, y1, label='y1随x的变化')  
plt.plot(x, y2, label='y2随x的变化')

  
# 添加标题和标签  
plt.title('y1和y2随x的变化关系')  
plt.xlabel('xxxxx')  
plt.ylabel('yyyyyyy')  
plt.legend()  # 显示图例，如果没有标签，可以删去
  
# 显示网格  
plt.grid(True)  
  
# 保存图形为图片文件，支持多种格式，如PNG, JPEG, SVG, PDF, EPS等  
plt.savefig('y1和y2随x的变化关系.png')  # 将图片保存为PNG格式  
  
# 显示图形（在Jupyter Notebook等环境中）  
plt.show()
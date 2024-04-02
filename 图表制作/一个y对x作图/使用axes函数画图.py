import matplotlib.pyplot as plt  # 导入绘图模块
import pandas as pd  # 导入数据分析模块
from matplotlib import rcParams  # 导入绘图模块
from matplotlib.ticker import MultipleLocator, FormatStrFormatter # 导入刻度模块

# 设置中文字体和负号正常显示
# chinese_font = font.Font(family="SimSun", size=14)  # 这里以“宋体”为例
# rcParams['axes.unicode_minus'] = False
rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体  
# rcParams['font.size'] = 18
rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 创建数据
data_path = '一个y对x作图/y对x数据.xlsx'  # 使用了“/”
df = pd.read_excel(data_path)
x = df['年份']
y = df['粮食产量（万吨）']

# 创建绘图窗口
fig,ax = plt.subplots()
fig.set_size_inches(8, 6)

# 绘制曲线
ax.plot(x, y, label='粮食产量对年份作图', color='r', linewidth=2) # 绘制曲线


# 设置坐标轴刻度
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(5000))
# ax.xaxis.set_major_formatter(FormatStrFormatter('%d')) # 设置y轴标签格式

# 设置坐标轴标签
ax.set_xlabel('年份') # 设置x轴标签
ax.set_ylabel('粮食产量') # 设置y轴标签
ax.set_title('粮食产量对年份的关系图')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)  
ax.legend(loc='upper left', bbox_to_anchor=(0.3, 0.65))  # 需要同时指定两个参数
fig.tight_layout()  # 调整图形布局使其更美观  
# 保存图形为图片文件，支持多PNG, JPEG, SVG, PDF, EPS等  
# plt.savefig('粮食产量对年份的关系图.png')  # 将图片保存为PNG格式，位置在上一层  

plt.show()
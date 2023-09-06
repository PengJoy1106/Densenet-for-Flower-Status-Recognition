import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件并存储数据到DataFrame对象
df = pd.read_csv('results/Non_Infectious_Diseases_Results/train_results.csv')

df = df.iloc[:102, :]

# 绘制损失值曲线图
plt.plot(df.index, df['Loss'], label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# 绘制准确率曲线图
plt.plot(df.index, df['Accuracy'], label='Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# 绘制学习率曲线图
plt.plot(df.index, df['Rate'], label='Learning Rate')
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.legend()
plt.show()
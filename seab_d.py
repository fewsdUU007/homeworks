import seaborn as sns
import matplotlib.pyplot as plt

# Пример данных
tips = sns.load_dataset("tips")

sns.set(style="whitegrid")
g = sns.relplot(
    x="total_bill",
    y="tip",
    hue="smoker",
    data=tips,
    height=7,
    aspect=1.25
)

g.fig.suptitle('Пример графика с использованием Seaborn')
plt.show()

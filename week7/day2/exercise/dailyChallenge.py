import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
# data = pd.DataFrame(data, columns=['x', 'y'])
# for col in 'xy':
#     plt.hist(data[col], normed=True, alpha=0.5)
# plt.title("Matplotlib histogram")
# plt.show()


df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.head()
df.info()

sns.barplot(df['Pclass'])
plt.show()
# mean point plot
sns.catplot(x="Pclass", y="Age", hue="Sex", data=df, kind="point");
plt.show()

# scatter plot
sns.relplot(x="Pclass", y="Age",hue="Sex", style="Survived", data=df);
plt.show()

# Line Plot
sns.relplot(x="Pclass", y="Age", kind="line", data=df);
plt.show()

# Linear Regression Plot
sns.lmplot(x="Pclass", y="Age",data=df);
plt.show()


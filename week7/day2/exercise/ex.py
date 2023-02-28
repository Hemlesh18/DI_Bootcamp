import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    plt.hist(data[col], normed=True, alpha=0.5)
plt.title("Matplotlib histogram")
plt.show()

import seaborn as sns
for col in 'xy':
    sns.kdeplot(data[col], shade=True)
plt.title("Seaborn kdeplot")
plt.show()


sns.distplot(data['x'])
sns.distplot(data['y']);
plt.title("Seaborn distplot")
plt.show()

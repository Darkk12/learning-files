import numpy as np
import matplotlib.pyplot as plt

mean = [0, 0]
cov = [[1, 2], [2, 5]]
rand = np.random.RandomState(42)
x = rand.multivariate_normal(mean, cov, (100))
plt.style.use('seaborn')

indices = np.random.choice(x.shape[0], 20, replace=False)
print(indices)
#plt.show()
selection = x[indices]
plt.scatter(x[:, 0], x[:, 1])
plt.scatter(selection[:, 0], selection[:, 1], facecolor = 'red',s=100, alpha=0.3)
plt.show()
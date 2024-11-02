import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
import matplotlib.pyplot as plt
import os

data = np.array([[3, -1.5, 2, -5.4], [0, 4, -0.3, 2.1], [1, 3.3, -1.9, -4.3]])

#均值移除
data_standardized = preprocessing.scale(data)
print(f'mean = {data_standardized.mean(axis=0)}')
print(f'std deviation = {data_standardized.std(axis=0)}')

#归一化
data_normalized = preprocessing.normalize(data, norm='l1')
print(f'normalized data: {data_normalized}')

#二值化
data_binarized = preprocessing.binarize(data, threshold=1.4)
print(f'binarized data: {data_binarized}')

# 修改文件路径
print(f'__file__: {__file__}') 
a = os.path.abspath(__file__)
print(f'a: {a}')
current_dir = os.path.dirname(a)
print(f'current_dir: {current_dir}')
filename = os.path.join(current_dir, 'data.txt')
print(f'filename: {filename}')
X = []
y = []

with open(filename, 'r') as file:
    for line in file:
        values = [float(s) for s in line.split(',')]
        X.append(values[:-1])
        y.append(values[-1])

# print(f'X: {X}')
# print(f'y: {y}')

num_training = int(0.8 * len(X))
num_test = len(X) - num_training

#训练数据和测试数据
X_train = X[:num_training]
y_train = y[:num_training]

X_test = X[num_training:]
y_test = y[num_training:]

#创建线性回归对象
linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train, y_train)
y_pred = linear_regressor.predict(X_test)

plt.figure()
plt.scatter(y_test, y_pred, color='red', marker='o', label='test data')
plt.plot([-10, 50], [-10, 50], 'k--', linewidth=3)
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.legend(loc='upper left')
plt.show()

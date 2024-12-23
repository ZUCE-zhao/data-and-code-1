import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB

# 读取数据并跳过第一行表头
path = r"E:\codes\line_force\data"
filename = 'data2.csv'
with open(path + '\\' + filename) as temp_f:
    col_count = [len(l.split(",")) for l in temp_f.readlines()]
column_names = [i for i in range(max(col_count))]
data = pd.read_csv(path + '\\' + filename, skiprows=1, skip_blank_lines=True, header=None, names=column_names)
print(column_names)

print("病态步态数据规模：", data.shape)
X = data.iloc[:, :6]
y = data.iloc[:, 7].apply(lambda x: 1 if x > 183 else 0)

# 分割数据集，60%训练集，40%验证集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# 初始化高斯朴素贝叶斯模型
model = GaussianNB()

# 训练模型
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估模型性能
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Confusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)

# 如果需要查看预测结果和实际结果的对比，可以使用以下代码
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

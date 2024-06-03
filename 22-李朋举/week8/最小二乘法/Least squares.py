import pandas as pd

'''
使用`pandas`库的`read_csv()`函数来读取 CSV 文件。
    1. `sales = pd.read_csv('train_data.csv')`：这行代码指定了要读取的 CSV 文件的路径。文件名为`train_data.csv`在当前工作目录下。
    2. `sep='\s*,\s*'`：指定了 CSV 文件的分隔符,分隔符是空格和逗号的组合。`\s*`表示匹配任意数量的空格，而`,`表示匹配逗号。
                       `\s*,\s*`表示匹配由空格和逗号组成的序列。
    3. `engine='python'`：这行代码指定了使用 Python 的内置 CSV 解析器来读取 CSV 文件。这是`read_csv()`函数的一个参数，
                          默认值为`c`，表示使用 C 语言实现的 CSV 解析器。选择`python`引擎可以更灵活地处理各种分隔符和数据类型。
     返回scales，`read_csv()`函数会读取`train_data.csv`文件，并将其解析为一个`DataFrame`对象，然后将该`DataFrame`对象赋值给变量`sales`。
    `DataFrame`是`pandas`库中的一个数据结构，用于处理二维的表格型数据。
'''
sales = pd.read_csv('train_data.csv', sep='\s*,\s*', engine='python')  # 读取CSV
'''
           X   Y
        0  1   6
        1  2   5
        2  3   7
        3  4  10
'''
X = sales['X'].values  # 存csv的第一列 [ 1  2  3 4 ]
Y = sales['Y'].values  # 存csv的第二列 [ 6  5  7 10]

# 初始化赋值
s1 = 0
s2 = 0
s3 = 0
s4 = 0
n = 4  # 你需要根据的数据量进行修改

# 循环累加
for i in range(n):
    s1 = s1 + X[i] * Y[i]  # X*Y，求和
    s2 = s2 + X[i]  # X的和
    s3 = s3 + Y[i]  # Y的和
    s4 = s4 + X[i] * X[i]  # X**2，求和

# 计算斜率和截距
k = (s2 * s3 - n * s1) / (s2 * s2 - s4 * n)
b = (s3 - k * s2) / n
print("Coeff: {} Intercept: {}".format(k, b))
# y=1.4x+3.5

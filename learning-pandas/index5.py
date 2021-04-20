import pandas as pd

df1 = pd.read_excel("learning-pandas/data/physical_measurement2.xlsx")
df2 = pd.read_excel("learning-pandas/data/blood_type.xlsx")

# 重複を削除
df3 = df1.drop_duplicates()

# print(df2.head(3))
"""
    id blood type
0    1          B
1    2          A
2    3          A
"""

# print(df3.head(3))
"""
    id  age      height  weight     sex
0    3   18  172.814251    75.0    male
1    2   18  159.925427    51.0    male
2    1   18         NaN    45.0    male
"""

# df3にf2をマージ。onの値に紐づける
# print(pd.merge(df3, df2, on="id"))
"""
    id  age      height  weight     sex blood type
0    3   18  172.814251    75.0    male          A
1    2   18  159.925427    51.0    male          A
2    1   18         NaN    45.0    male          B
"""

df4 = pd.read_csv("learning-pandas/data/brownian_1.csv", delimiter=",")
# print(df4.head(3))
"""
   Unnamed: 0         0         1         2         3
0           0  0.000000  0.000000  0.000000  0.000000
1           1  2.660897  0.308681  1.150186  0.080541
2           2  3.598515  0.108084  1.751230 -0.317608
"""

df5 = pd.read_csv("learning-pandas/data/brownian_2.csv", delimiter=",")
# print(df5.head(3))
"""
   Unnamed: 0         0         1         2         3
0          11 -0.259006  0.340749  0.328479 -1.408017
1          12 -0.352558 -0.170449  0.110878 -1.120390
2          13  1.421724  0.828752  1.887549 -1.998712
"""

# df4の下にdf5を合体
print(pd.concat([df4, df5]))
"""
    Unnamed: 0         0         1         2         3
0            0  0.000000  0.000000  0.000000  0.000000
1            1  2.660897  0.308681  1.150186  0.080541
2            2  3.598515  0.108084  1.751230 -0.317608
3            3  2.985630 -0.819268  0.730809 -2.676886
4            4  3.768073 -0.303198  0.678676 -3.187084
5            5  2.202500 -0.043631  0.454354 -3.415329
6            6  2.344100 -0.161837 -0.719099 -1.168604
7            7  0.686527  0.180138 -0.339193 -2.117601
8            8  0.770178  0.066214  0.865318 -0.971832
9            9  1.045955  0.812871 -0.261247 -0.613309
10          10  1.095013  0.098859 -0.562678 -0.960184
0           11 -0.259006  0.340749  0.328479 -1.408017
1           12 -0.352558 -0.170449  0.110878 -1.120390
2           13  1.421724  0.828752  1.887549 -1.998712
"""

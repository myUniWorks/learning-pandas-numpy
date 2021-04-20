# ビニング
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.show()

df_x = pd.read_csv("learning-pandas/data/brownian_x.csv",
                   delimiter=",", index_col=0)
df_y = pd.read_csv("learning-pandas/data/brownian_y.csv",
                   delimiter=",", index_col=0)

df_d = (df_x ** 2 + df_y ** 2) ** 0.5

# print(df_d.head(3))
"""
          0         1         2         3         4         5         6  ...        93        94        95        96        97        98        99
0  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  ...  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000  0.000000
1  2.664995  1.624617  1.466082  0.624082  0.483413  1.773034  1.175548  ...  2.016019  1.023372  1.640556  0.072268  1.697960  0.790099  1.198749
2  3.700546  1.001601  1.754423  0.515130  1.198450  1.987591  2.914376  ...  1.756776  2.243826  0.423914  0.087729  1.082146  3.060686  1.619214
"""

# df_d.iloc[-1].hist(bins=25)

# 0~90まで10刻み
bins = np.arange(0, 90, 10)

# print(bins)
"""
[ 0 10 20 30 40 50 60 70 80]
"""

data = pd.cut(df_d.iloc[-1], bins)

# print(data)
"""
どの区分に存在するか
0     (10, 20]
1     (10, 20]
2     (40, 50]
3     (50, 60]
4     (10, 20]
        ...   
95    (20, 30]
96    (20, 30]
97    (20, 30]
98    (40, 50]
99    (20, 30]
Name: 500, Length: 100, dtype: category
Categories (8, interval[int64]): [(0, 10] < (10, 20] < (20, 30] < (30, 40] < (40, 50] < (50, 60] <
                                  (60, 70] < (70, 80]]
"""

# print(pd.value_counts(data))
"""
区分ごとのカウント
(20, 30]    29
(10, 20]    23
(30, 40]    16
(40, 50]    13
(0, 10]     10
(50, 60]     5
(60, 70]     4
(70, 80]     0
Name: 500, dtype: int64
"""

# print(pd.value_counts(data, sort=False))
"""
(0, 10]     10
(10, 20]    23
(20, 30]    29
(30, 40]    16
(40, 50]    13
(50, 60]     5
(60, 70]     4
(70, 80]     0
Name: 500, dtype: int64
"""

# df_d.iloc[-1].hist()


plt.style.use("ggplot")

df = pd.read_excel("learning-pandas/data/multiple_data.xlsx")

# print(df)
"""
     X         Y  param
0    0  0.730928      1
1    1  0.720069      1
2    2  0.709225      1
3    3  0.698262      1
4    4  0.687277      1
..  ..       ...    ...
75  15  0.431922      4
76  16  0.413629      4
77  17  0.395994      4
78  18  0.378900      4
79  19  0.362336      4
"""

groups = df.groupby("param")

# for name, group in groups:
#     plt.scatter(group["X"], group["Y"], label=name)
# plt.legend()
"""
パラーメーターごとのグラフを描画
"""

df_1 = groups.get_group(1)

# print(df_1.head())
"""
paramが1のみ
     X         Y  param
0    0  0.730928      1
1    1  0.720069      1
2    2  0.709225      1
3    3  0.698262      1
4    4  0.687277      1
"""

plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(9).reshape(3, 3))

# print(df1)
"""
スプレッドシート風に生成。
行方向：index、列方向；colum

   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8
"""

df2 = pd.DataFrame(np.arange(9).reshape(3, 3), index=[
                   "a", "b", "c"], columns=["A", "B", "C"])

# print(df2)
"""
   A  B  C
a  0  1  2
b  3  4  5
c  6  7  8
"""

# print(df2["A"])
"""
a    0
b    3
c    6
Name: A, dtype: int64
"""

# print(df2.index)
"""
Index(['a', 'b', 'c'], dtype='object')
"""

# print(df2.columns)
"""
Index(['A', 'B', 'C'], dtype='object')
"""

# print(df2.columns[0])
"""
A
"""

# print(df2.values)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""

# print(df2.shape)
"""
(3, 3)
"""

# print(df2.shape[0])
"""
3
"""

df3 = pd.read_excel("learning-pandas/data/physical_measurement.xlsx")

"""
df3.head()→上から5行(デフォルト)取得
df3.tail(3)→下から3行取得
"""

# print(df3["height"])
"""
指定したカラムの列だけ取得
0     172.814251
1     159.925427
2     143.287031
3     172.929461
4     163.959781
5     169.007453
・・・省略
"""

# print(df3["height"].mean())
"""
平均を取得
159.0123135601849
"""

# print(df3[df3["height"] > 170])
"""
ブールインデックス参照で170cm以上のデータのみを取得
ブールインデックス参照：[] の中にインデックスを書く代わりに論理値(True/False)の配列を書くとその論理値がTrueに該当する箇所の要素をピックアップしたndarrayを新しく作ってくれる。
    age      height  weight     sex
0    18  172.814251    75.0    male
3    18  172.929461    64.0    male
6    18  181.663292    65.0    male
9    18  173.386830    55.0    male
12   18  171.594600    66.0    male
16   18  178.845219    74.0    male
18   18  179.785433    68.0    male
20   18  175.338770    70.0    male
24   18  174.872408    56.0  female
41   18  173.957967    55.0  female
"""


df_f = df3[df3["sex"] == "female"]

# print(df_f.head())
"""
    age      height  weight     sex
21   18  145.206173    42.0  female
22   18  152.000383    45.0  female
23   18  146.732318    50.0  female
24   18  174.872408    56.0  female
25   18  145.042772    60.0  female
"""

# ヒストグラム
df_f["height"].hist(bins=30)

# 下記でグラフを表示
# plt.show()

df4 = pd.DataFrame(np.arange(16).reshape(4, 4))

# print(df4)
"""
    0   1   2   3
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
"""

df4_rename = df4.rename(index={0: "a", 1: "b", 2: "c", 3: "d"},
                        columns={0: "A", 1: "B", 2: "C", 3: "D"})

# print(df4_rename)
"""
    A   B   C   D
a   0   1   2   3
b   4   5   6   7
c   8   9  10  11
d  12  13  14  15
"""

# df4_reindex = df4.reindex(columns=["D", "C", "B", "A"])

# print(df4_reindex)
"""
*調査
D   C   B   A
0 NaN NaN NaN NaN
1 NaN NaN NaN NaN
2 NaN NaN NaN NaN
3 NaN NaN NaN NaN
"""

# print(df4_rename.iloc[:, 1])
"""
数字でアクセス
a     1
b     5
c     9
d    13
Name: B, dtype: int64
"""

# print(df4_rename["B"]["c"])
"""
9
"""

# print(df4_rename["B"][1:])
"""
b     5
c     9
d    13
Name: B, dtype: int64
"""

df5 = pd.read_excel(
    "learning-pandas/data/physical_measurement2.xlsx", index_col=0)

# print(df5.head(3))
"""
index_colで特定の列をindexに指定
    age      height  weight     sex
id
3    18  172.814251    75.0    male
2    18  159.925427    51.0    male
1    18         NaN    45.0    male
"""

df5_sorted = df5.sort_index()

# print(df5_sorted.head(3))
"""
    age      height  weight   sex
id                               
1    18         NaN    45.0  male
2    18  159.925427    51.0  male
3    18  172.814251    75.0  male
"""

# print(df5_sorted.dropna().head(3))
"""
NaNがある行を削除
    age      height  weight   sex
id                               
2    18  159.925427    51.0  male
3    18  172.814251    75.0  male
4    18  172.929461    64.0  male
"""

# print(df5_sorted.fillna(value=-1.0).head(3))
"""
NaNを特定の値に変更
    age      height  weight   sex
id                               
1    18   -1.000000    45.0  male
2    18  159.925427    51.0  male
3    18  172.814251    75.0  male
"""

# print(df5_sorted.fillna(method="ffill"))
"""
NaNの直前の値をコピー。1行目は前の値がないので、NaN
1    18         NaN    45.0    male
2    18  159.925427    51.0    male
・
・
・
13   18  171.594600    66.0    male
14   18  171.594600    59.0    male
"""

df5_meaned = df5_sorted.fillna(value=df5_sorted.mean())

# print(df5_meaned.head(6))
"""
NaNを平均値に置き換え
1    18  159.516527  45.000000    male
2    18  159.925427  51.000000    male
3    18  172.814251  75.000000    male
4    18  172.929461  64.000000    male
5    18  163.959781  55.000000    male
5    18  163.959781  55.000000    male
"""

df5_new_meaned = df5_meaned.drop_duplicates()

# print(df5_new_meaned.head(6))
"""
重複値を削除
    age      height  weight   sex
id                               
1    18  159.516527    45.0  male
2    18  159.925427    51.0  male
3    18  172.814251    75.0  male
4    18  172.929461    64.0  male
5    18  163.959781    55.0  male
6    18  169.007453    57.0  male
"""

df5_new_meaned["sex2"] = df5_new_meaned["sex"].apply(
    lambda x: np.where(x == "male", 1, -1))

# print(df5_new_meaned)
"""
    age      height     weight     sex  sex2
id                                          
1    18  159.516527  45.000000    male     1
・
・
・
12   18  156.622645  54.243902  female    -1
"""

del df5_new_meaned["sex"]

# print(df5_new_meaned.head(3))
"""
特定の列を削除
    age      height     weight  sex2
id                                  
1    18  159.516527  45.000000     1
2    18  159.925427  51.000000     1
3    18  172.814251  75.000000     1
"""

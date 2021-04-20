import pandas as pd

# マルチインデックス

# df = pd.read_excel("learning-pandas/data/bussei.xlsx")

# print(df)
"""
DensityやViscosityがvalueの一部として扱われてしまう
    Unnamed: 0    water Unnamed: 2      air Unnamed: 4
0  Temperature  Density  Viscosity  Density  Viscosity
1            0    999.8   0.001792    1.293   1.71e-05
2            5     1000   0.001519     1.27  1.734e-05
3           10    999.7   0.001307    1.247  1.759e-05
4           15    999.1   0.001138    1.226  1.784e-05
5           20    998.2   0.001002    1.204  1.808e-05
6           25      997    0.00089    1.185  1.832e-05
7           30    996.5  0.0007973    1.165  1.856e-05
"""

# 以下は仕様変更により動作しないので、マルチインデックスのインポートは調べておく

# df1 = pd.read_excel("learning-pandas/data/bussei.xlsx",
#                     index_col=[0, 1])
df1 = pd.read_excel("learning-pandas/data/bussei.xlsx", index_col=1)

# print(df1)
"""
  Unnamed: 0_level_0   water               air          
         Temperature Density Viscosity Density Viscosity
0                  0   999.8  0.001792   1.293  0.000017
1                  5  1000.0  0.001519   1.270  0.000017
2                 10   999.7  0.001307   1.247  0.000018
3                 15   999.1  0.001138   1.226  0.000018
4                 20   998.2  0.001002   1.204  0.000018
5                 25   997.0  0.000890   1.185  0.000018
6                 30   996.5  0.000797   1.165  0.000019
"""

# print(df1["water"])
"""
   Density  Viscosity
0    999.8   0.001792
1   1000.0   0.001519
2    999.7   0.001307
3    999.1   0.001138
4    998.2   0.001002
5    997.0   0.000890
6    996.5   0.000797
"""

# print(df1["air"])

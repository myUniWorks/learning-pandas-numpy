# Series
import numpy as np
import pandas as pd

s1 = pd.Series(np.arange(4))

# print(s1)
"""
左がindex(key)、右がvalue
0    0
1    1
2    2
3    3
dtype: int64
"""

s2 = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])

# print(s2)
"""
a    1
b    2
c    3
d    4
e    5
dtype: int64
"""

# print(list(s2))
"""
リストに変換できる
[1, 2, 3, 4, 5]
"""

num_dict = {"a": 1, "b": 2, "c": 3}

# print(pd.Series(num_dict))
"""
ディクショナリーからシリーズを作成
a    1
b    2
c    3
dtype: int64
"""

s3 = pd.Series([])

s3["a"] = 1

# print(s3)
"""
a    1
dtype: int64
"""

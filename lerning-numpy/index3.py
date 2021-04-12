import numpy as np

arr1 = np.arange(9)

# 必要に応じてarrayの形になる演算をブロードキャストという

# print(3 * arr1)
"""
すべての要素に対して計算
[ 0  3  6  9 12 15 18 21 24]
"""

# print(1 + arr1)
"""
[1 2 3 4 5 6 7 8 9]
"""

# ユニバーサル関数：ndarrayで返す

print(np.sin(arr1))
"""
[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
 -0.2794155   0.6569866   0.98935825]
"""
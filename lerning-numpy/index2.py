import numpy as np

arr1 = np.arange(9).reshape([3,3])

# print(arr1)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""

# print(arr1[0, 0])
"""
0
"""

# print(arr1[0,1])
"""
1
"""

# print(arr1[:, 1])
"""
[1 4 7]
"""

# 以下、ブルーインデックス参照(純粋なリストではできない)

# print(arr1 > 4)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]

[[False False False]
 [False False  True]
 [ True  True  True]]
"""

print(arr1[arr1 > 4])
"""
[5 6 7 8]
"""
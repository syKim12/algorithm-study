from copy import deepcopy
array = [[1,2],[3,4]]
deepcopy_array = deepcopy(array)

new_array = []
for i in array:
    new_array.append(i)

new_array[0][0] = 0
print(array)
print("shallow copy:", new_array)
print("deep copy:", deepcopy_array)

"""
RESULT
[[0, 2], [3, 4]]
shallow copy: [[0, 2], [3, 4]]
deep copy: [[1, 2], [3, 4]]
"""
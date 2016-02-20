import numpy as np
#Sort array by column
sort_array = np.array([[368,1],[47,2],[144,3],[83,4]])
print("Original Array:")
print(sort_array)
sorted_array = sort_array[sort_array[:,0].argsort()]
print("Sorted Array:")
print(sorted_array)
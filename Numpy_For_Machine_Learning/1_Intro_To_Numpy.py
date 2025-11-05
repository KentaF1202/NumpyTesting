import numpy as np

# Python lists can accept many types of variables but are computationally slower

list1 = [1,2,3,4,5]
list2 = ["John Doe", 41, list1, True]


# Numpy - Numeric Python
# ndarray = n-dimensional arrays

# Make numpy array
np1 = np.array([0,1,2,3,4,5,6,7])
print(np1)

#Shape of numpy array
print(np1.shape)

# Range array
np2 = np.arange(10)
print(np2)

# Arange can have start, stop, step
# Keep in mind it includes the start but excludes the stop i.e. [start, stop)
np3 = np.arange(0,10,2)
print(np3)

# Zero numpy array
# Keep in mind they are init as float 0.
np4 = np.zeros(10)
print(np4)

# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

# Full
np6 = np.full((10), 6)
print(np6)

# Multidimensional Full
np7 = np.full((2,10), 6)
print(np7)

# Convert python lists to np
np8 = np.array(list1)
print(np8)

# Access member of numpy array
print(np8[0])
import numpy as np

# Slicing numpy arrays
np1 = np.array([1,2,3,4,5,6,7,8])

# Return 3,4,5
print(np1[2:5])

# Return from something until the end
print(np1[3:])

# Return negative slices
# Can only iterate left to right
print(np1[-3:-1])

# Steps
print(np1[1:5:2])

# Steps on the entire array
print(np1[::2])

# Slice a 2-d array
np2 = np.array([
    [1,2,3,4,5],[6,7,8,9,10]
    ])
# Pull out one item
print(np2[0][3])
print(np2[0,3])
# Pull from singular
print(np2[0:1, 1:3])
# Pull from multiple
print(np2[0:2, 1:3])
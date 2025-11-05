import numpy as np

# Numpy Universal Functions
np1 = np.array([1,2,-3,4,5,-6,7,8,9])
print(np1)

# Square root of each element
print(np.sqrt(np1))

# Absolute Value 
print(np.absolute(np1))

# Exponents
#[2.71828183e+00 7.38905610e+00 4.97870684e-02 5.45981500e+01 1.48413159e+02 2.47875218e-03 1.09663316e+03 2.98095799e+03 8.10308393e+03]
# Each number when natural logged is equal to the corresponding original array index
print(np.exp(np1))

# Logarithms
print(np.log(np1))

# Min/Max
# Factors in negative
print(np.max(np1))
print(np.min(np1))

# Sign positive or negative
print(np.sign(np1))

# Trig sin cos tan
print(np.sin(np1))
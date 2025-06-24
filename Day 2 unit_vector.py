import numpy as np

# Define vectors
a = np.array([6, 2])
b = np.array([3, -1])

# Subtract vectors
result = a - b
print("a - b =", result)

# Norm (magnitude)
norm = np.linalg.norm(a)
print("||a|| =", round(norm, 2))

# Unit vector of 'a'
unit_a = a / norm
print("unit vector of a:", np.round(unit_a, 2))

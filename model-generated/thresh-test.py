import numpy as np

# 1. 0 * np.nan
print("1: ", 0 * np.nan)  # Output: nan


# 2. np.nan == np.nan
print("2: ", np.nan == np.nan)  # Output: False


# 3. np.inf == np.nan
print("3: " , np.inf == np.inf)  # Output: True


# 4. np.nan - np.nan
print("4: " , np.nan - np.nan)  # Output: nan


# 5. np.nan in set([np.nan])
print("5: " , np.nan in set([np.nan]))  # Output: True


# 6. 0.30000000000000004 == 3 * 0.1
print("6: " , 0.30000000000000004 == 3 * 0.1)  # Output: True
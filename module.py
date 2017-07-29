import math
import random
import statistics

# .pow(Number, Exponent) --> To the power of...
print(math.pow(2, 3))

# print a random number .randint(base, max)
print(random.randint(0, 100))

# mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

# median
print(statistics.median(nums))

# mode
print(statistics.mode(nums))
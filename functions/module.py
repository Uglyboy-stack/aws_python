import math

absolute = 5.999
floor_test = 198.91

result1 = math.fabs(absolute)
result2 = math.ceil(floor_test)

print(result1, "is the absolute value of", absolute)
print(result2, "is the floored value of", floor_test)
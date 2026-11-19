# 1. Error message:
# TypeError: can only concatenate str (not "int") to str
#
# 2. What caused it:
# I tried to add an integer (5) directly to a string ("10") without converting the string to an integer first.
#
# 3. How I fixed it:
# I wrapped the string in int() so both values are integers before adding them together.

num_str = "10"
result = int(num_str) + 5
print(result)

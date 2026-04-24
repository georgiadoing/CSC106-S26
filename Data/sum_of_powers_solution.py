# Kristina Striegnitz
#
# Calculate the sum of the first n integers raised to a given power.

def sum_of_powers(power, n):
    """Sum up the first n integers raised to the given power.
    E.g. sum_of_powers(2, 5) -> 55 (1 + 4 + 9 + 16 + 25)
    """
    sum = 0
    for i in range(1, n+1):
        sum += i**power
    return sum
    

### DO NOT DELETE THIS LINE: beg testing

# Use this area if you want to add some function calls with different
# parameter values to test your function definition.

# E.g. the sum of the first five squares should be 55.
print(sum_of_powers(2, 5))



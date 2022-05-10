# Century From Year
# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def century(year):
    age = str(year)
    if len(age) > 2:
        if int(age[-2]) >= 1 or int(age[-1]) >= 1:
            cent = int(age[0:-2]) + 1
        else:
            cent = int(age[0:2])
    else:
        cent = 1
    return cent
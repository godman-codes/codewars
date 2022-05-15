# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# Beginner - Reduce but Grow

def grow(arr):
    total = 1
    for i in range(0, len(arr)):
        total = total * arr[i]
    return total
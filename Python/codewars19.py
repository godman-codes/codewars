# Story
# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

# Task
# Write a function that returns both the minimum and maximum number of the given list/array.

# # The highest profit wins!

def min_max(lst):
    luk = []
    mark = sorted(lst)
    luk.append(mark[0])
    luk.append(mark[-1])
    return luk
    
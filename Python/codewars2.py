# # Reversed Strings
# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'


def solution(string):
    new = list(string)
    new ="".join(new[::-1])
    return new
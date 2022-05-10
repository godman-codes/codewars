# Fake Binary
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    love = str(x)
    k = []
    for i in love:
        if int(i) < 5:
            k.append('0')
        else:
            k.append('1')
    return ''.join(k)
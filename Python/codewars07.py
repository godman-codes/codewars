from math import ceil
def dig_pow(n, p):
   mark = [x for x in str(n) ]
   # print(mark)
   count = 0
   for i in mark:
      # print(p)
      count += int(i)**(p)
      p+=1
      # print(count)
   positive = count / n
   if ceil(positive) == positive:
      return int(positive)
   else:
      return -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
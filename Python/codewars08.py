from math import ceil, floor
def solution(number):
   new_list = []
   count = 0
   for i in range(number + 1):
      sum_three = i/3
      sum_five = i/5
      ceil_three = ceil(sum_three)
      floor_three = floor(sum_three)
      ceil_five = ceil(sum_five)
      floor_five = floor(sum_five)
      if (ceil_three) == (floor_three):
         if ceil_three not in new_list:
            new_list.append(ceil_three)
            count += ceil_three
      if (ceil_five) == (floor_five):
         if ceil_five not in new_list:
            new_list.append(ceil_five)
            count += ceil_five
   return (new_list)
   return (count)
solution(466)
   
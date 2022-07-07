from math import ceil, floor
def solution(number):
    if number < 0:
        return 0
    new_list = []
    count = 0
    for i in range(number):
        sum_three = i/3
        sum_five = i/5
        ceil_three = ceil(sum_three)
        floor_three = floor(sum_three)
        ceil_five = ceil(sum_five)
        floor_five = floor(sum_five)
        if (ceil_three) == (floor_three):
            if i not in new_list:
                new_list.append(i)
                count += i
        if (ceil_five) == (floor_five):
            if i not in new_list:
                new_list.append(i)
                count += i
    print(new_list)
    print(count)

    #one liner
def solution2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0 )
  
   
solution(10)
   
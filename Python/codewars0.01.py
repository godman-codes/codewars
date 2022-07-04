def square_digits(num):
   str_num = str(num)
   newList = []
   for i in str_num:
      newList.append(str(int(i) ** 2))
   return int(''.join(newList))
print(square_digits(9119))
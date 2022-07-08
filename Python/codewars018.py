def increment_string(string_2):
   new_string2 = string_2[::-1]
   # print(new_string2)
   position = 0
   nums = '0123456789'
   new_list = []
   for i in range(len(new_string2)):
      if new_string2[i] not in nums:
         # print(new_string2[i])
         position += i
         new_list.append(new_string2[:i][::-1])
         break
   if new_list == []:
      done = pass_random('')
      # print(done)
      # print(new_string2[:position][::-1], 's')
      return new_string2[:position][::-1] + done
   else:
      done = pass_random(new_list[0])
      # print(done)
      # print(new_string2[position:][::-1], 's')
      return new_string2[position:][::-1] + done

def pass_random(string):
   pointer = 0
   if string == '':
      return '1'
   elif string.isalpha():
      return string + '1'
   new_mark = []
   for i in range(len(string)):
      if not string[i].isalpha() and string[i] != '0':
         pointer += i
         new_mark.append(string[i:])
         break
   if new_mark == [] and '0' in string: 
      return string[:-1] + '1'
   sums = str(int(new_mark[0])+1)
   if (len(sums) > len(new_mark[0])) and string[:pointer] != '' and string[:pointer][-1] == '0':
      return string[:pointer][:-1] + sums
   elif (len(sums) > len(new_mark[0])) and string[:pointer] != '' and string[:pointer][-1] != '0':
      return string[:pointer]+ sums
   elif (len(sums) > len(new_mark[0])) and string[:pointer] == '':
      return sums
   elif len(sums) == len(new_mark[0]):
      return string[:pointer]+ sums



print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar1"))
print(increment_string("foobar00"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))
print(increment_string(""))
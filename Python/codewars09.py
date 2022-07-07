def solution(s):
   new_list = []
   if len(s) == 1:
      new_list.append(s[0] + '_')
      return new_list
   for i in range(0,len(s), 2):
      if i != len(s) -1:
         new_list.append(s[i]+s[i+1])
      else:
         new_list.append(s[i] + '_')
   return(new_list)

print(solution('x'))
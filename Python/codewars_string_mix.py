class reversor:
   def __init__(self, obj):
      self.obj = obj

   def __eq__(self, other):
      return other.obj == self.obj

   def __lt__(self, other):
         return other.obj < self.obj
def mix(s1, s2):
   new_list = []
   for i in  set(s1).union(set(s2)):
      if i.isalpha() and i.islower():
         count1 = s1.count(i)
         count2 = s2.count(i)
         if (count1 > 1 or count2 > 1) and count1 > count2:
            new_list.append([count1, f'1:{i*count1}'])
         elif (count1 > 1 or count2 > 1) and count1 < count2:
            new_list.append([count2, f'2:{i*count2}'])
         elif (count1 > 1 or count2 > 1) and count1 == count2:
            new_list.append([count1, f'=:{i*count1}'])
   return '/'.join([x[1] for x in sorted(new_list, reverse=True, key= lambda x: (x[0], reversor(x[1])))])


print(mix("Are they here", "yes, they are here"))
#  "2:eeeee/2:yy/=:hh/=:rr"
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"))
# 2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz
# print(mix("looping is fun but dangerous", "less dangerous than coding"))
# "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
# print(mix(" In many languages", " there's a pair of functions"))
# print(mix("Lords of the Fallen", "gamekult"))
# print(mix("codewars", "codewars"))
# print(mix("A generation must confront the looming ", "codewarrs"))

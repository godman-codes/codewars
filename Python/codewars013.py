def anagrams(word, words):
   # return [x if len(word) not set(word).symmetric_difference(set(x))]
   new_list = []
   for i in words:
      if ''.join(sorted(word)) == ''.join(sorted(i)):
         if not set(word).symmetric_difference(set(i)):
            new_list.append(i)
   return new_list
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
#  , ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
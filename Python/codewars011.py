def first_non_repeating_letter(string):
   string2 = string.copy().lower()
   for x in range(string2):
      if string2.count(string2[x]) == 1:
         return string[x]
def to_camel_case(text):
   if text == '':
      return ''
   for i in text:
      if not i.isalpha():
         text = text.replace(i, ' ')
   # print(text)
   newText2= text.split(' ')
   for i in range(len(newText2)):
      if i == 0:
         continue
      else:
         newText2[i] = newText2[i].capitalize()
         newText2[0] += newText2[i]
   
   return newText2[0]

to_camel_case('')
to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case("A-B-C")
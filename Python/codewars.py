def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def to_postfix (infix):
   """Convert infix to postfix"""
   newStack = [x for x in infix[::-1]]
   print(newStack)
   stack = []
   output = []
   while newStack:
      if newStack[-1].isnumeric():
         output.append(newStack[-1])
         newStack.pop(-1)
      else:
         # stack.append(newStack[-1])
         current = newStack.pop(-1)
         if len(stack) >= 2:
            if current == ')':
               if stack[-2] == '(' and stack[-1] not in '()':
                  print(stack)
                  stack.pop(-1)
                  output.append(stack.pop(-1))
                  stack.pop(-1)
         elif len(stack) >=2:
            if stack[-1] in '-+' and stack[-2] in '*/^':
               output.append(stack.pop(-2))
            elif stack[-1] in '-+' and stack[-2] in '-+':
               output.append(stack.pop(-2))
            elif stack[-1] in '*/' and stack[-2] in '*/':
               output.append(stack.pop(-2))
            elif stack[-1] in '*/' and stack[-2] == '^':
               output.append(stack.pop(-2))
            elif stack[-1] == stack[-2]:
               output.append(stack.pop(-2))
   if len(stack) > 0:
      newOutput = output + stack[::-1]
      print(listToString(newOutput))
   else:
      print(listToString(output))

to_postfix("2+7*5")
to_postfix("5+(6-2)*9+3^(7-1)")
to_postfix("1^2^3")
to_postfix("(5-4-1)+9/5/2-7/1/7")
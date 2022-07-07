import re
def valid_braces(string):
   # print(string)
   checker = re.compile(r'\(\)|\{\}|\[\]|')
   checkers_result = checker.findall(string)
   if string == "":
      return f"True string is empty"
   elif len(checkers_result) > 0:
      string = string.replace("()", "")
      string = string.replace("[]", "")
      string = string.replace("{}", "")
      return valid_braces(string)
   elif len(checkers_result) == 0:
      return False

print(valid_braces("()"))
print(valid_braces("(}"))
print(valid_braces("[]"))
# # print(valid_braces("[(])"))
# print(valid_braces("{}"))
# print(valid_braces("{}()[]"))
# print(valid_braces("([{}])"))
# print(valid_braces("([}{])"))
# print(valid_braces("{}({})[]"))
# print(valid_braces("(({{[[]]}}))"))
# print(valid_braces("(((({{"))
# print(valid_braces(")(}{]["))
# print(valid_braces("())({}}{()][]["))
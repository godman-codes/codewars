import re
def printer_error(s):
   errors = re.compile(r'[^abcdefghijklm]')
   return f'{len(errors.findall(s))}/{len(s)}'

print(printer_error('adsdddhfhfnvmdkdodiifiufhbnkdxx'))
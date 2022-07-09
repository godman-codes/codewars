def format_duration(seconds):
   if seconds == 0:
      return 'now'
   if seconds == 1:
      return '1 second'
   elif seconds < 60:
      return f'{seconds} seconds'
   elif seconds == 31536000:
      return '1 year'
   elif seconds == 60:
      return '1 minute'
   elif seconds == 86400:
      return '1 day'
   elif seconds == 3600:
      return '1 hour'
   years = seconds//31536000
   days = (seconds%31536000)//86400
   hours = ((seconds%31536000)%86400)//3600
   minutes = (((seconds%31536000)%86400)%3600)//60
   secondz = (((seconds%31536000)%86400)%3600)%60

   new_seconds = lambda x : f'{secondz} seconds'\
      if x > 1 else (f'{secondz} second' if x == 1\
         else '')
   new_minutes = lambda x : f'{minutes} minutes' if x > 1\
      else (f'{minutes} minute' if x == 1\
         else '')
   new_hours = lambda x : f'{hours} hours' if x > 1\
      else (f'{hours} hour' if x == 1\
         else '')
   new_days = lambda x : f'{days} days' if x > 1\
      else (f'{days} day' if x == 1\
         else '')
   new_years = lambda x : f'{years} years' if x > 1\
      else (f'{years} year' if x == 1\
         else '')
   output_list = [new_years(years), new_days(days), new_hours(hours), new_minutes(minutes), new_seconds(secondz)]
   new_list = list(filter(None, output_list))
   if len(new_list) == 1:
      return new_list[0]
   if len(new_list) == 2:
      return f'{new_list[0]} and {new_list[1]}'
   if len(new_list) == 3:
      return f'{new_list[0]}, {new_list[1]} and {new_list[2]}'
   if len(new_list) == 4:
      return f'{new_list[0]}, {new_list[1]}, {new_list[2]} and {new_list[3]}'
   if len(new_list) == 5:
      return f'{new_list[0]}, {new_list[1]}, {new_list[2]}, {new_list[3]} and {new_list[4]}'
      



print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))
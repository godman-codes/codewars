def make_readable(seconds):
   hours = int(seconds/3600)
   minutes = int(int(seconds%3600)/60)
   seconds = (seconds%3600)%60
   if len(str(hours)) < 2:
      hours = '0' + str(hours)
   if len(str(minutes)) < 2:
      minutes = '0' + str(minutes)
   if len(str(seconds)) < 2:
      seconds = '0' + str(seconds)
   return f'{str(hours)}:{str(minutes)}:{str(seconds)}'

print(make_readable(0))
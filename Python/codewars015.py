def ips_between(start, end):
   start_list = start.split('.')
   # print(start_list)
   end_list = end.split('.')
   # print(end_list)
   first_difference = ((int(end_list[0]) - int(start_list[0]))*256*256*256)
   # print(first_difference)
   second_difference = ((int(end_list[1]) - int(start_list[1]))*256*256)
   # print(second_difference)
   third_difference = ((int(end_list[2]) - int(start_list[2]))*256)
   # print(third_difference)
   fourth_difference = int(end_list[3]) - int(start_list[3])
   # print(fourth_difference)
   cumulative = first_difference + second_difference + third_difference + fourth_difference
   
   return cumulative

ips_between("10.0.0.0", "10.0.0.50")
ips_between("20.0.0.10", "20.0.1.0")
# cumulative = ((int(end_list[0]) - int(start_list[0]))*256*256*256) + ((int(end_list[1]) - int(start_list[1]))*266*256) + ((int(end_list[2]) - int(start_list[2]))*266) + (int(end_list[0]) - int(start_list[0]))
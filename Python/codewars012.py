def sort_array(source_array):
   odd_list = [x for x in source_array if x % 2 == 1]
   odd_list2 = odd_list.copy()
   odd_list = sorted(odd_list, reverse=True)
   for i in range(len(source_array)):
      if source_array[i] in odd_list2:
         source_array[i] = odd_list.pop()
   return source_array


sort_array([5, 3, 2, 8, 1, 4])
sort_array([5, 3, 1, 8, 0])
sort_array([])
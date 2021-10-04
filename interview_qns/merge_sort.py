def merge_sort(data):
  
  print("The passed data: {0}".format(data))
  if len(data) <= 1:
      return
  
  mid = len(data) // 2
  print("The mid: {0}".format(mid))
  
  left_data = data[:mid]
  print("The left data: {0}".format(left_data))
  right_data = data[mid:]
  print("The right data: {0}".format(right_data))
  
  merge_sort(left_data)
  print("The left data after calling merge sort: {0}".format(left_data))
  merge_sort(right_data)
  print("The right data after calling merge sort: {0}".format(right_data))
  
  left_index = 0
  right_index = 0
  data_index = 0
  
  while left_index < len(left_data) and right_index < len(right_data):
    print("the left index: {0} --- the right index: {1}".format(left_index, right_index))
    print("the left data: {0} ----- the right data: {1}".format(left_data, right_data))
    if left_data[left_index] < right_data[right_index]:
      data[data_index] = left_data[left_index]
      print("the data - left comparison: {0}".format(data))
      left_index += 1
    else:
      data[data_index] = right_data[right_index]
      print("the data - right comparison: {0}".format(data))
      right_index += 1
    
    data_index += 1
  
  print("Data out of while loop: {0}".format(data))
  
  if left_index < len(left_data):
    print("The left del data: {0}".format(data[data_index:]))
    del data[data_index:]
    data += left_data[left_index:]
  elif right_index < len(right_data):
    print("The right del data: {0}".format(data[data_index:]))
    del data[data_index:]
    data += right_data[right_index:]
    
  print("The sorted data")
  print(data)
  
d = [2,1,4,6,89,65,34,21,34,55,44,32,70]
merge_sort(d)

def forward_fill(values: list) -> list:
  
  if len(values) == 0:
    return values
  
  arr = [values[0]]
  for i in range(1,len(values)):
    if values[i] is None:
      arr.append(arr[i-1])
    else:
      arr.append(values[i])
  return arr
      

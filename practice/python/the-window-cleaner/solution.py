def longest_unique_substr(s):
  
  dict_str = {}
  valid_str = []
  
  for k,v in enumerate(s):
    if v not in valid_str:
      valid_str.append(v)
    else:
      dict_str[len(valid_str)] = valid_str
      valid_str = []
      valid_str.append(v)
  else:
    dict_str[len(valid_str)] = valid_str
     
  return max(dict_str) if len(dict_str) > 0 else 0

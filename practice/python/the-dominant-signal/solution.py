def most_frequent(items: list) -> list:
  items_dict = {}
  for i in items:
    items_dict[i] = items_dict.get(i, 0) + 1
  
  # for k,v in items_dict.items():
  #   if v == max(list(items_dict.values())):
  #     return 
    
  return sorted(k for k,v in items_dict.items() if v == max(list(items_dict.values())))
  
  # return max(list(items_dict.values())) if len(items_dict) > 0 else []

def dedup_preserve_order(items: list) -> list:
  items_dict = {}
  for k,v in enumerate(items):
    if v in items_dict:
      continue
    else:
      items_dict[v] = k
  return [x[0] for x in sorted(items_dict.items(), key=lambda x: x[1])]
